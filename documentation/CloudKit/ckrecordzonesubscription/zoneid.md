# zoneID

**Framework**: CloudKit  
**Kind**: property

The ID of the record zone that the subscription queries.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var zoneID: CKRecordZone.ID { get }
```

#### Discussion

This property applies to query-based subscriptions and zone-based subscriptions. Specifying a record zone ID limits the scope of the query to only the records in that zone. For zone-based subscriptions, the query includes all records in the specified record zone. For a query-based subscription, the query includes only records of a specific type in the specified record zone.

For zone-based subscriptions, CloudKit sets this property’s value automatically. For all other subscription types, the default value is `nil`. If you want to scope your query-based subscription to a specific record zone, you must assign a value explicitly.

## See Also

- [var recordType: CKRecord.RecordType?](ckrecordzonesubscription/recordtype-1fuqo.md)
  The type of record that the subscription queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/zoneid)*