# intentHandlingStatus

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The current state of the interaction.

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
var intentHandlingStatus: INIntentHandlingStatus { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INIntentHandlingStatus intentHandlingStatus;
```

*macOS*

```objc
@property (atomic, readonly) INIntentHandlingStatus intentHandlingStatus;
```

## Discussion

This property reflects your app’s current progress (if any) toward completing the interaction. The value of this property is set automatically using the code in the response object. The default value of this property is [`INIntentHandlingStatus.unspecified`](../inintenthandlingstatus/unspecified.md).

## See Also

### Accessing Interaction Attributes
- [var direction: INInteractionDirection](./direction.md)
  The direction in which information flowed to or from the device.
- [var dateInterval: DateInterval?](./dateinterval.md)
  The time at which the interaction started and its duration.
- [var identifier: String](./identifier.md)
  The unique identifier of the interaction.
- [var groupIdentifier: String?](./groupidentifier.md)
  The unique identifier of the interaction’s group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/intenthandlingstatus)*