# init(subscriptionID:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a named subscription for all records in a database.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS
- watchOS 6.0+
- Swift 4.2+

## Declaration

```swift
convenience init(subscriptionID: CKSubscription.ID)
```

## Parameters

- `subscriptionID`: The subscription’s name. CloudKit uniques subscriptions by subscriptionID. You must not provide an empty string.

## See Also

### Creating a Database Subscription
- [convenience init()](./init%28%29.md)
  Creates an empty database subscription.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates a database subscription from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/init(subscriptionid:))*