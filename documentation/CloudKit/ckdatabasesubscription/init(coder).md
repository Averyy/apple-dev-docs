# init(coder:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a database subscription from a serialized instance.

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

- `aDecoder`: The object that decodes the serialized database subscription.

## See Also

### Creating a Database Subscription
- [convenience init()](./init%28%29.md)
  Creates an empty database subscription.
- [convenience init(subscriptionID: CKSubscription.ID)](./init%28subscriptionid%29.md)
  Creates a named subscription for all records in a database.
- [- initWithSubscriptionID:](./initwithsubscriptionid_.md)
  Creates a named subscription for all records in a database.
- [+ new](./new.md)
  Creates an empty database subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/init(coder:))*