# HMHomeHubState

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

The possible states of the home hub.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum HMHomeHubState
```

```c
enum HMHomeHubState : NSUInteger;
```

## Topics

### Specifying the State
- [HMHomeHubState.connected](./hmhomehubstate/connected.md)
  The home hub is connected.
- [HMHomeHubState.disconnected](./hmhomehubstate/disconnected.md)
  The home hub is disconnected.
- [HMHomeHubState.notAvailable](./hmhomehubstate/notavailable.md)
  No home hub is present.
### Initializers
- [init?(rawValue: UInt)](./hmhomehubstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Querying the state of a home hub
- [var homeHubState: HMHomeHubState](./hmhome/homehubstate.md)
  The state of the home hub.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomehubstate)*