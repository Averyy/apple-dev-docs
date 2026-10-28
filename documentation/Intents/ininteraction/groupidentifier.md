# groupIdentifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the interaction’s group.

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
var groupIdentifier: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSString * groupIdentifier;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSString * groupIdentifier;
```

## Mentions

- [Deleting Donated Shortcuts](../../SiriKit/deleting-donated-shortcuts.md)

## Discussion

Assigning the same identifier string to two or more interaction objects defines a group. You can use the group identifier later to delete all interactions with that identifier. The default value of this property is `nil`, which means that the interaction is not associated with a group.

## See Also

### Accessing Interaction Attributes
- [var intentHandlingStatus: INIntentHandlingStatus](./intenthandlingstatus.md)
  The current state of the interaction.
- [var direction: INInteractionDirection](./direction.md)
  The direction in which information flowed to or from the device.
- [var dateInterval: DateInterval?](./dateinterval.md)
  The time at which the interaction started and its duration.
- [var identifier: String](./identifier.md)
  The unique identifier of the interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/groupidentifier)*