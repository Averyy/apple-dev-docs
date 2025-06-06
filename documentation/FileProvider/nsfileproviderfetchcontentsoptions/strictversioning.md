# strictVersioning

**Framework**: File Provider  
**Kind**: property

An option that indicates the system requires an exact match of the requested item’s version.

**Availability**:
- macOS 12.3+

## Declaration

```swift
static var strictVersioning: NSFileProviderFetchContentsOptions { get }
```

#### Discussion

If the system includes this option when calling your [`fetchPartialContents(for:version:request:minimalRange:aligningTo:options:completionHandler:)`](nsfileproviderpartialcontentfetching/fetchpartialcontents(for:version:request:minimalrange:aligningto:options:completionhandler:).md) method, you must provide the requested version of the item. If you can’t provide the requested version, pass a [`NSFileProviderError.Code.versionNoLongerAvailable`](nsfileprovidererror/code/versionnolongeravailable.md) error to the completion handler instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderfetchcontentsoptions/strictversioning)*