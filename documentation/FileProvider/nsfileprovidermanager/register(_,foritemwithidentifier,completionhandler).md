# register(_:forItemWithIdentifier:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Registers the URL session task responsible for the specified item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func register(_ task: URLSessionTask, forItemWithIdentifier identifier: NSFileProviderItemIdentifier, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func register(_ task: URLSessionTask, forItemWithIdentifier identifier: NSFileProviderItemIdentifier) async throws
```

```objc
- (void) registerURLSessionTask:(NSURLSessionTask *) task forItemWithIdentifier:(NSFileProviderItemIdentifier) identifier completionHandler:(void (^)(NSError *error)) completion;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func register(_ task: URLSessionTask, forItemWithIdentifier identifier: NSFileProviderItemIdentifier) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## See Also

### Performing actions
- [class func placeholderURL(for: URL) -> URL](./placeholderurl%28for%29.md)
  Returns a placeholder URL for a given document URL.
- [class func writePlaceholder(at: URL, withMetadata: NSFileProviderItem) throws](./writeplaceholder%28at,withmetadata%29.md)
  Writes a document placeholder with the provided metadata.
- [func signalEnumerator(for: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./signalenumerator%28for,completionhandler%29.md)
  Alerts the system to changes in the specified folder’s content.
- [func waitForChanges(below: NSFileProviderItemIdentifier, completionHandler: ((any Error)?) -> Void)](./waitforchanges%28below,completionhandler%29.md)
  Requests a notification after the system completes all the specified changes.
- [func globalProgress(for: Progress.FileOperationKind) -> Progress](./globalprogress%28for%29.md)
  Returns a progress object that tracks either the uploading or downloading of items from the File Provider extension’s remote storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/register(_:foritemwithidentifier:completionhandler:))*