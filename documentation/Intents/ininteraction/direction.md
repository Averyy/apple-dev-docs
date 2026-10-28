# direction

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The direction in which information flowed to or from the device.

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
var direction: INInteractionDirection { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign) INInteractionDirection direction;
```

*macOS*

```objc
@property (atomic, assign) INInteractionDirection direction;
```

## Discussion

Use this property to convey whether the interaction involved information moving to or from the current device. For example, starting a video call from this device indicates an outgoing interaction, which means you should set this property to [`INInteractionDirection.outgoing`](../ininteractiondirection/outgoing.md). The default value of this property is [`INInteractionDirection.unspecified`](../ininteractiondirection/unspecified.md).

## See Also

### Accessing Interaction Attributes
- [var intentHandlingStatus: INIntentHandlingStatus](./intenthandlingstatus.md)
  The current state of the interaction.
- [var dateInterval: DateInterval?](./dateinterval.md)
  The time at which the interaction started and its duration.
- [var identifier: String](./identifier.md)
  The unique identifier of the interaction.
- [var groupIdentifier: String?](./groupidentifier.md)
  The unique identifier of the interaction’s group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/direction)*