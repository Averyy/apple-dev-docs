# init(zoneID:)

**Framework**: CloudKit  
**Kind**: init

Creates a subscription for all records in the specified record zone.

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
convenience init(zoneID: CKRecordZone.ID)
```

#### Discussion

The subscription that this method returns is a zone-based subscription that generates push notifications when CloudKit changes any of the specificed record zone’s records.

## Parameters

- `zoneID`: The ID of the record zone that contains the records you want to monitor. This parameter must not be  .

## See Also

- [convenience init(zoneID: CKRecordZone.ID, subscriptionID: CKSubscription.ID)](ckrecordzonesubscription/init(zoneid:subscriptionid:).md)
  Creates a named subscription for all records in the specified record zone.
- [init(coder: NSCoder)](ckrecordzonesubscription/init(coder:).md)
  Creates a zone-based subscription from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/init(zoneid:))*