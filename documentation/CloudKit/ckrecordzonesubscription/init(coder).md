# init(coder:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a zone-based subscription from a serialized instance.

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
init(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Parameters

- `aDecoder`: The coder for decoding the serialized record zone subscription.

## See Also

### Creating a Zone-Based Subscription
- [convenience init(zoneID: CKRecordZone.ID)](./init%28zoneid%29.md)
  Creates a subscription for all records in the specified record zone.
- [convenience init(zoneID: CKRecordZone.ID, subscriptionID: CKSubscription.ID)](./init%28zoneid,subscriptionid%29.md)
  Creates a named subscription for all records in the specified record zone.
- [- initWithZoneID:subscriptionID:](./initwithzoneid_subscriptionid_.md)
  Creates a named subscription for all records in the specified record zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzonesubscription/init(coder:))*