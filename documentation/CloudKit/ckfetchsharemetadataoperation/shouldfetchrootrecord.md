# shouldFetchRootRecord

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether to retrieve the root record.

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
var shouldFetchRootRecord: Bool { get set }
```

#### Discussion

For a shared record hierarchy, set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to include the root record in the fetched share metadata. CloudKit ignores this property for a shared record zone because, unlike a shared record hierarchy, it doesn’t have a nominated root record.

The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var shareURLs: [URL]?](ckfetchsharemetadataoperation/shareurls.md)
  The URLs of the shares to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/shouldfetchrootrecord)*