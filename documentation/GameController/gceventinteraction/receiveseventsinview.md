# receivesEventsInView

**Framework**: Game Controller  
**Kind**: property

A Boolean value that determines whether events are delivered exclusively through the Game Controller framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
var receivesEventsInView: Bool { get set }
```

#### Discussion

If `YES`, events of the types specified by `handledEventTypes` are delivered both through the Game Controller framework and as UIKit event objects to your app’s views and gesture recognizers.

If `NO`, events of the types specified by `handledEventTypes` are delivered  through the Game Controller framework.

The default value of this property is `NO`. This property has no effect if `handledEventTypes` is `GCUIEventTypeNone`.

## See Also

- [struct GameControllerEventHandlingOptions](gamecontrollereventhandlingoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gceventinteraction/receiveseventsinview)*