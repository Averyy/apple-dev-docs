# identifier

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the interaction.

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
var identifier: String { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy) NSString * identifier;
```

## Mentions

- [Deleting Donated Shortcuts](../../SiriKit/deleting-donated-shortcuts.md)

#### Discussion

This property is initialized to a new UUID at initialization time, but you can change it if you want to use a different identification scheme. The identifier you assign to this property must be unique within your app.

## See Also

### Accessing Interaction Attributes
- [var intentHandlingStatus: INIntentHandlingStatus](./intenthandlingstatus.md)
  The current state of the interaction.
- [var direction: INInteractionDirection](./direction.md)
  The direction in which information flowed to or from the device.
- [var dateInterval: DateInterval?](./dateinterval.md)
  The time at which the interaction started and its duration.
- [var groupIdentifier: String?](./groupidentifier.md)
  The unique identifier of the interaction’s group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/identifier)*