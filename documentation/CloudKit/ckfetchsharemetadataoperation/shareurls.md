# shareURLs

**Framework**: CloudKit  
**Kind**: property

The URLs of the shares to fetch.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var shareURLs: [URL]? { get set }
```

#### Discussion

Use this property to view or change the URLs of the shares to fetch. If you intend to specify or change this property’s value, do so before you execute the operation or submit it to a queue.

## See Also

- [var shouldFetchRootRecord: Bool](ckfetchsharemetadataoperation/shouldfetchrootrecord.md)
  A Boolean value that indicates whether to retrieve the root record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/shareurls)*