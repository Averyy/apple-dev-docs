# dateInterval

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The time at which the interaction started and its duration.

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
var dateInterval: DateInterval? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSDateInterval * dateInterval;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSDateInterval * dateInterval;
```

#### Discussion

Use this property to reflect time-related information for the interaction. For example, you could use this property to reflect the duration of a phone call or the timestamp of a message. At initialization time, the date portion is set to the current time and the duration is set to `0`.

## See Also

### Accessing Interaction Attributes
- [var intentHandlingStatus: INIntentHandlingStatus](./intenthandlingstatus.md)
  The current state of the interaction.
- [var direction: INInteractionDirection](./direction.md)
  The direction in which information flowed to or from the device.
- [var identifier: String](./identifier.md)
  The unique identifier of the interaction.
- [var groupIdentifier: String?](./groupidentifier.md)
  The unique identifier of the interaction’s group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/dateinterval)*