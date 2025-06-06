# stageTransition

**Framework**: AppKit  
**Kind**: property

The transition value for the stage of a pressure gesture event.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
var stageTransition: CGFloat { get }
```

#### Discussion

This property is specifically intended to provide a value for the transition animation between the stages of a pressure gesture event.

Gesture events of type [`NSEvent.EventType.pressure`](nsevent/eventtype/pressure.md) go through stages, and transitions occur between these stages. This property indicates a transition value between the current stage and the next or prior stage.

This value is distinct from pressure. It immediately resets to `0` as soon as a stage transition occurs. However, this value does not then immediately begin to fluctuate. The value only starts to change as a new stage begins to approach. It then continues to rise or fall throughout the transition, until that new stage is reached.

As pressure increases for the gesture and a new stage approaches, this property provides a value between `0` and `1`, indicating the approach of the next stage. When pressure is reduced for the gesture and a new stage is approached, this property provides a value between `0` and `-1`, indicating the approach of the current stage’s release.

## See Also

- [NSEvent.EventType](nsevent/eventtype.md)
  Constants for the types of events that responder objects can handle.
- [NSEvent.EventType.pressure](nsevent/eventtype/pressure.md)
  An event that reports a change in pressure on a pressure-sensitive device.
- [var pressure: Float](nsevent/pressure.md)
  A normalized value that indicates the degree of pressure applied to an appropriate input device.
- [var stage: Int](nsevent/stage.md)
  A value that indicates the stage of a pressure gesture event.
- [var pressureBehavior: NSEvent.PressureBehavior](nsevent/pressurebehavior-swift.property.md)
  The behavior and progression for a pressure event.
- [NSEvent.PressureBehavior](nsevent/pressurebehavior-swift.enum.md)
  These constants describe the behavior and progression of a pressure gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/stagetransition)*