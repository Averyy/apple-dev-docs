# MPFeedbackCommandEvent

**Framework**: Media Player  
**Kind**: class  
**Role**: Class

An event requesting a change in the feedback setting.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class MPFeedbackCommandEvent
```

```objc
@interface MPFeedbackCommandEvent : MPRemoteCommandEvent
```

## Topics

### Determining the type of feedback action
- [var isNegative: Bool](./mpfeedbackcommandevent/isnegative.md)
  A Boolean value that indicates whether an app should perform a negative command appropriate to the target.

## Relationships

### Inherits From
- [MPRemoteCommandEvent](./mpremotecommandevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to feedback and rating events
- [class MPFeedbackCommand](./mpfeedbackcommand.md)
  An object that reflects the feedback state for the playing item.
- [class MPRatingCommand](./mpratingcommand.md)
  An object that provides a detailed rating for the playing item.
- [class MPRatingCommandEvent](./mpratingcommandevent.md)
  An event requesting a change in the rating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommandevent)*