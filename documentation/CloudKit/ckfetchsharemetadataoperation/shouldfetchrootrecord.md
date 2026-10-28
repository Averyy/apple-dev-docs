# shouldFetchRootRecord

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) BOOL shouldFetchRootRecord;
```

## Discussion

For a shared record hierarchy, set this property to [`true`](../../Swift/true.md) to include the root record in the fetched share metadata. CloudKit ignores this property for a shared record zone because, unlike a shared record hierarchy, it doesn’t have a nominated root record.

The default value is [`false`](../../Swift/false.md).

## See Also

### Configuring the Operation
- [var shareURLs: [URL]?](./shareurls.md)
  The URLs of the shares to fetch.
- [rootRecordDesiredKeys](./rootrecorddesiredkeys-7gvr5.md)
  The fields to return when fetching the root record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/shouldfetchrootrecord)*