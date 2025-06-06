# CarKeyRemoteControlSession.ContinuationStrategy

**Framework**: CarKey  
**Kind**: enum

Strategy to use on reception of a continuation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
enum ContinuationStrategy
```

## Topics

### Operators
- [static func == (CarKeyRemoteControlSession.ContinuationStrategy, CarKeyRemoteControlSession.ContinuationStrategy) -> Bool](carkeyremotecontrolsession/continuationstrategy/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [CarKeyRemoteControlSession.ContinuationStrategy.automatic](carkeyremotecontrolsession/continuationstrategy/automatic.md)
  Auto-confirm any incoming continuation requests until the requested action is stopped or completed with no intervention from the client.
- [CarKeyRemoteControlSession.ContinuationStrategy.manual](carkeyremotecontrolsession/continuationstrategy/manual.md)
  Give your app control over the incoming continuation requests and allow to exchange data with the vehicle.
### Instance Properties
- [var hashValue: Int](carkeyremotecontrolsession/continuationstrategy/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](carkeyremotecontrolsession/continuationstrategy/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](carkeyremotecontrolsession/continuationstrategy/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/carkeyremotecontrolsession/continuationstrategy)*