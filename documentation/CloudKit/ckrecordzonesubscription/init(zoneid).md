# init(zoneID:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a subscription for all records in the specified record zone.

**Availability**:
- iOS 10.0+ - Deprecated in 10.0
- iPadOS 10.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.12
- tvOS 10.0+ - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 6.0

## Declaration

```swift
convenience init(zoneID: CKRecordZone.ID)
```

```objc
- (instancetype) initWithZoneID:(CKRecordZoneID *) zoneID;
```

#### Discussion

The subscription that this method returns is a zone-based subscription that generates push notifications when CloudKit changes any of the specified record zone’s records.

## Parameters

- `zoneID`: The ID of the record zone that contains the records you want to monitor. This parameter must not be `nil`.

## See Also

### Creating a Zone-Based Subscription
- [convenience init(zoneID: CKRecordZone.ID, subscriptionID: CKSubscription.ID)](./init%28zoneid,subscriptionid%29.md)
  Creates a named subscription for all records in the specified record zone.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a zone-based subscription from a serialized instance.
- [- initWithZoneID:subscriptionID:](./initwithzoneid_subscriptionid_.md)
  Creates a named subscription for all records in the specified record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/init(zoneid:))*