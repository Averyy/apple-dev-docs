# INInteractionDirection

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating whether the app is providing or receiving information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INInteractionDirection
```

```c
enum INInteractionDirection : NSInteger;
```

## Topics

### Constants
- [INInteractionDirection.unspecified](./ininteractiondirection/unspecified.md)
  An unspecified direction.
- [INInteractionDirection.outgoing](./ininteractiondirection/outgoing.md)
  An interaction in which information is sent from the device.
- [INInteractionDirection.incoming](./ininteractiondirection/incoming.md)
  An interaction in which information is received on the device.
### Initializers
- [init?(rawValue: Int)](./ininteractiondirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum INIntentHandlingStatus](./inintenthandlingstatus.md)
  Constants indicating the current state of the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteractiondirection)*