# init(subscriptionID:)

**Framework**: CloudKit  
**Kind**: init

Creates a named subscription for all records in a database.

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
convenience init(subscriptionID: CKSubscription.ID)
```

## Parameters

- `subscriptionID`: The subscription’s name. It must be unique in the container, and must not be an empty string.

## See Also

- [convenience init()](ckdatabasesubscription/init.md)
  Creates an empty database subscription.
- [init(coder: NSCoder)](ckdatabasesubscription/init(coder:).md)
  Creates a database subscription from a serialized instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/init(subscriptionid:))*