# rootRecordDesiredKeys

**Framework**: CloudKit  
**Kind**: property

The fields to return when fetching the root record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
var rootRecordDesiredKeys: [CKRecord.FieldKey]? { get set }
```

#### Discussion

For a shared record hierarchy, and when [`shouldFetchRootRecord`](ckfetchsharemetadataoperation/shouldfetchrootrecord.md) is [`true`](https://developer.apple.com/documentation/swift/true), set this property to specify which of the root record’s fields the operation fetches. Use `nil` to fetch the entire record. CloudKit ignores this property for a shared record zone because, unlike a hierarchy, it doesn’t have a nominated root record.

The default value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsharemetadataoperation/rootrecorddesiredkeys-3xrex)*