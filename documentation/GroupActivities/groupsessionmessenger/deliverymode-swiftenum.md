# GroupSessionMessenger.DeliveryMode

**Framework**: Group Activities  
**Kind**: enum

The transmission characteristics to apply to the delivery of messages.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum DeliveryMode
```

## Topics

### Getting the delivery mode options
- [GroupSessionMessenger.DeliveryMode.reliable](groupsessionmessenger/deliverymode-swift.enum/reliable.md)
  An attempt to ensure the delivery of messages to known participants.
- [GroupSessionMessenger.DeliveryMode.unreliable](groupsessionmessenger/deliverymode-swift.enum/unreliable.md)
  A best-effort attempt to deliver the message to known participants.
### Comparing the delivery mode options
- [static func != (Self, Self) -> Bool](groupsessionmessenger/deliverymode-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (GroupSessionMessenger.DeliveryMode, GroupSessionMessenger.DeliveryMode) -> Bool](groupsessionmessenger/deliverymode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](groupsessionmessenger/deliverymode-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](groupsessionmessenger/deliverymode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](groupsessionmessenger/deliverymode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/deliverymode-swift.enum)*