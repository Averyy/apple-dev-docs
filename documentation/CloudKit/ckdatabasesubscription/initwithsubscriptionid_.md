# initWithSubscriptionID:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a named subscription for all records in a database.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (instancetype) initWithSubscriptionID:(CKSubscriptionID) subscriptionID;
```

## Parameters

- `subscriptionID`: The subscription’s name. It must be unique in the container, and must not be `nil` or an empty string.

## See Also

### Creating a Database Subscription
- [convenience init()](./init%28%29.md)
  Creates an empty database subscription.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a database subscription from a serialized instance.
- [+ new](./new.md)
  Creates an empty database subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/initwithsubscriptionid:)*