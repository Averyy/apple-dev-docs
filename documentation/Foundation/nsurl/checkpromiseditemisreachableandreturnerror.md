# checkPromisedItemIsReachableAndReturnError(_:)

**Framework**: Foundation  
**Kind**: method

Returns whether the promised item can be reached.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func checkPromisedItemIsReachableAndReturnError(_ error: NSErrorPointer) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the promised item is reachable; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method behaves identically to [`checkResourceIsReachableAndReturnError(_:)`](nsurl/checkresourceisreachableandreturnerror(_:).md), but works on promised items. A promised item is not guaranteed to have its contents in the file system until you use a file coordinator to perform a coordinated read on its URL, which causes the contents to be downloaded or otherwise generated. Promised item URLs are returned by various APIs, including:

- A metadata query using either the [`NSMetadataQueryUbiquitousDataScope`](nsmetadataqueryubiquitousdatascope.md) or [`NSMetadataQueryUbiquitousDocumentsScope`](nsmetadataqueryubiquitousdocumentsscope.md) scopes
- The contents of the directory returned by the file manager’s `URLForUbiquitousContainerIdentifier:`
- The URL inside the accessor block of a coordinated read or write operation that used the [`immediatelyAvailableMetadataOnly`](nsfilecoordinator/readingoptions/immediatelyavailablemetadataonly.md), [`forDeleting`](nsfilecoordinator/writingoptions/fordeleting.md), [`forMoving`](nsfilecoordinator/writingoptions/formoving.md), or [`contentIndependentMetadataOnly`](nsfilecoordinator/writingoptions/contentindependentmetadataonly.md) options

You must use this method instead of `checkResourceIsReachableAndReturnError` for any URLs returned by these methods.

## Parameters

- `error`: The error that occurred when the promised item could not be reached.

## See Also

- [func checkResourceIsReachableAndReturnError(NSErrorPointer) -> Bool](nsurl/checkresourceisreachableandreturnerror(_:).md)
  Returns whether the resource pointed to by a file URL can be reached.
- [func getPromisedItemResourceValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: URLResourceKey) throws](nsurl/getpromiseditemresourcevalue(_:forkey:).md)
  Returns the value of the resource property for the specified key.
- [func promisedItemResourceValues(forKeys: [URLResourceKey]) throws -> [URLResourceKey : Any]](nsurl/promiseditemresourcevalues(forkeys:).md)
  Returns the resource values for the properties identified by specified array of keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurl/checkpromiseditemisreachableandreturnerror(_:))*