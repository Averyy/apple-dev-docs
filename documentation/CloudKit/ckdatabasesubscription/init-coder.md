# init(coder:)

**Framework**: CloudKit  
**Kind**: init

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

## Parameters

- `aDecoder`: The object that decodes the serialized database subscription.

## See Also

- [convenience init()](ckdatabasesubscription/init.md)
  Creates an empty database subscription.
- [convenience init(subscriptionID: CKSubscription.ID)](ckdatabasesubscription/init(subscriptionid:).md)
  Creates a named subscription for all records in a database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabasesubscription/init(coder:))*