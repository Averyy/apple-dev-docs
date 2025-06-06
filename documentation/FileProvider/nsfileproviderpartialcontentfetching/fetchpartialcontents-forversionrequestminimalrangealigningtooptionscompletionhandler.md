# fetchPartialContents(for:version:request:minimalRange:aligningTo:options:completionHandler:)

**Framework**: Fileprovider  
**Kind**: method  
**Required**: Yes

Tells the file provider to download the requested item from remote storage.

**Availability**:
- macOS 12.3+

## Declaration

```swift
func fetchPartialContents(for itemIdentifier: NSFileProviderItemIdentifier, version requestedVersion: NSFileProviderItemVersion, request: NSFileProviderRequest, minimalRange requestedRange: NSRange, aligningTo alignment: Int, options: NSFileProviderFetchContentsOptions = [], completionHandler: @escaping (URL?, NSFileProviderItem?, NSRange, NSFileProviderMaterializationFlags, (any Error)?) -> Void) -> Progress
```

#### Return Value

An item that tracks the extension’s progress.

#### Discussion

Implement this method to download a range of the specified file and pass it to the completion handler. If your file provider extension doesn’t implement this method, the system defaults to [`fetchContents(for:version:request:completionHandler:)`](nsfileproviderreplicatedextension/fetchcontents(for:version:request:completionhandler:).md).

The temporary file you provide must meet the following requirements:

- The temporary file can be a sparse file with noncontiguous ranges.
- You must properly align your `retrievedRange` base on the `alignment` parameter passed to this method. The starting location and length of the region you provide must be multiples of the `alignment` value. If your `retrievedRange` covers the rest of the file, then you don’t need to align the end. Just set its length based on the end of the file.
- The `retrievedRange` you provide must have the same location in the temp file that it does in the original. However, the sections before or after the `retrievedRange` can be empty, sparse ranges.
- Your `retrievedRange` must contain actual data with no holes, unless the original file is a sparse file, and the holes represent empty ranges in the original file.
- Your `retrievedRange` must cover the entire `requestedRange`; however, it can be larger than the `requestedRange` (either starting before, or extending after the `requestedRange`). For example, you could provide the entire file, if you have a cached version handy.

The system writes your entire `retrievedRange` to the user-visible file. You can adjust the size of the `retrievedRange` to optimize read latency and reduce the amount of data downloaded by your file provider extension.

If this is the first time the system has requested the file’s content, it sets the `options` parameter to an empty set. This indicates that it’s safe to return a different version than the requested version, if necessary.

However, when updating existing files, the system sets the `options` parameter to [`strictVersioning`](nsfileproviderfetchcontentsoptions/strictversioning.md). This prevents the system from accidentally writing mismatched pieces from different versions to the same file. If you can’t provide the requested version, pass a [`NSFileProviderError.Code.versionNoLongerAvailable`](nsfileprovidererror/code/versionnolongeravailable.md) error to the completion handler instead.

##### Concurrently Downloading Files

By default, the system calls the [`fetchPartialContents(for:version:request:minimalRange:aligningTo:options:completionHandler:)`](nsfileproviderpartialcontentfetching/fetchpartialcontents(for:version:request:minimalrange:aligningto:options:completionhandler:).md) method concurrently when there are multiple outstanding requests. This can include making multiple concurrent requests for different parts of the file.

You can control concurrent requests by setting the [`NSExtensionFileProviderDownloadPipelineDepth`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionFileProviderDownloadPipelineDepth) key in your extension’s `Info.plist` file. Set the value to the number of concurrent downloads the system can create per domain. This value must be between 1 and 128.

> **Note**:  You must set the [`NSExtensionFileProviderDownloadPipelineDepth`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionFileProviderDownloadPipelineDepth) key for each domain. The setting affects all requests for files in the specified domain.

##### Managing File Ownership

After receiving the `fileContents`, the system clones and deletes the file. Don’t mutate the corresponding file after calling the completion handler. If your extension needs to keep a copy of the content, create a clone of the content and pass the URL of the clone as the completion handler’s `fileContents` parameter.

If the extension or system crashes after you call the completion handler but before the system deletes the file, your temporary file may remain where you saved it. In this case, your extension must delete the file.

##### Disallowing Downloads

You can control which processes can request files. By default, the system automatically manages files based on its POSIX access control lists.

To prevent a process from accessing content from the extension’s domain, save an array of strings to the `NSFileProviderExtensionNonMaterializingProcessNames` [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) key. The system won’t fetch content if the requesting process’s name matches a string in this array.

- In macOS 11.0 and later, the system checks this list when a process reads a file using POSIX filesystem calls.
- In macOS 11.4 and later, the system also checks this list when a process reads a file using file coordination.

##### Handing Errors

If the system requests an item that your file provider extension doesn’t know about, pass the [`NSFileProviderError.Code.noSuchItem`](nsfileprovidererror/code/nosuchitem.md) error to the completion handler. The system then treats the item as if someone had removed the item from the domain, and it attempts to delete the file. If it can’t delete the item (for example, because the item has local changes) it recreates the item by calling your extension’s [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md) method.

If the user doesn’t have access to the file, you can pass an [`NSFileReadNoPermissionError`](https://developer.apple.com/documentation/foundation/nsfilereadnopermissionerror) error to the completion handler. The system then displays that error to the user.

Your extension can also pass [`NSFileProviderError.Code.notAuthenticated`](nsfileprovidererror/code/notauthenticated.md) and [`NSFileReadNoPermissionError`](https://developer.apple.com/documentation/foundation/nsfilereadnopermissionerror) errors if it can’t download the items because of the system or domain’s current state. In those cases, the system displays an error to the user, and doesn’t make another fetch request until the next time it receives an update notification about the item.

If you can’t provide the requested version for an item, provide a different version unless the system passed the [`strictVersioning`](nsfileproviderfetchcontentsoptions/strictversioning.md) key in the `options` parameter. In this case, pass a [`NSFileProviderError.Code.versionNoLongerAvailable`](nsfileprovidererror/code/versionnolongeravailable.md) error to the completion handler instead.

If your extension provides content that doesn’t match the requested version, the system detects the mismatch and treats it as a remote update. The system sends the requesting application an error, indicating that something has updated the item remotely. It then requests an updated copy of the item from your file provider.

The system considers all other errors as transient, and attempts to request the content again.

##### Canceling Downloads

Your implementation of this method must return a [`Progress`](https://developer.apple.com/documentation/Foundation/Progress) item that tracks your app’s progress while downloading the requested range. The system uses this item to show the progress to the user.

If the user cancels the operation, the system calls the progress item’s [`cancellationHandler`](https://developer.apple.com/documentation/foundation/progress/1408913-cancellationhandler) block. Use this block to stop fetching the item, because it’s no longer required.

## Parameters

- `itemIdentifier`: The item’s identifier.
- `requestedVersion`: The version of the item. The system always provides a specific version.
- `request`: An object that identifies the context of that request, such as the requesting app.
- `requestedRange`: The range given as a starting location and a length in bytes.
- `alignment`: A system defined alignment value. The start and end of the range of data you provide must be multiples of this value. The alignment value may change across reboots; however, the system guarantees that it’s a power of two.
- `options`: Options for the fetch range.
- `completionHandler`: A block that you call after downloading the item from your remote storage. You pass the following parameters:

## See Also

- [struct NSFileProviderFetchContentsOptions](nsfileproviderfetchcontentsoptions.md)
  Options for fetching a range of data from a file.
- [struct NSFileProviderMaterializationFlags](nsfileprovidermaterializationflags.md)
  Flags that provides additional information about the provided content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderpartialcontentfetching/fetchpartialcontents(for:version:request:minimalrange:aligningto:options:completionhandler:))*