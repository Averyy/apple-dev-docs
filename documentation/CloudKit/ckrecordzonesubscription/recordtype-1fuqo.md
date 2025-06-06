# recordType

**Framework**: CloudKit  
**Kind**: property

The type of record that the subscription queries.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 6.0+
- Swift 4.2+

## Declaration

```swift
var recordType: CKRecord.RecordType? { get set }
```

#### Discussion

This property only applies to query-based subscriptions. CloudKit sets its value when you create the subscription. For all other types of subscription, CloudKit ignores this property and sets its value to `nil`.

## See Also

- [var zoneID: CKRecordZone.ID](ckrecordzonesubscription/zoneid.md)
  The ID of the record zone that the subscription queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/recordtype-1fuqo)*