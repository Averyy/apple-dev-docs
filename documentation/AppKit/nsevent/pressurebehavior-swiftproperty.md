# pressureBehavior

**Framework**: AppKit  
**Kind**: property

The behavior and progression for a pressure event.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var pressureBehavior: NSEvent.PressureBehavior { get }
```

#### Discussion

This property describes the behavior and progression of an event of type [`NSEvent.EventType.pressure`](nsevent/eventtype/pressure.md). The value of this property indicates how the pressure event behaves, including actuations, pressure-level reporting, and stage transitions.

## See Also

- [class NSPressureConfiguration](nspressureconfiguration.md)
  An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.
- [NSEvent.EventType](nsevent/eventtype.md)
  Constants for the types of events that responder objects can handle.
- [NSEvent.EventType.pressure](nsevent/eventtype/pressure.md)
  An event that reports a change in pressure on a pressure-sensitive device.
- [init(pressureBehavior: NSEvent.PressureBehavior)](nspressureconfiguration/init(pressurebehavior:).md)
  Initializes a pressure configuration object with a specified pressure behavior.
- [var pressure: Float](nsevent/pressure.md)
  A normalized value that indicates the degree of pressure applied to an appropriate input device.
- [var stage: Int](nsevent/stage.md)
  A value that indicates the stage of a pressure gesture event.
- [var stageTransition: CGFloat](nsevent/stagetransition.md)
  The transition value for the stage of a pressure gesture event.
- [NSEvent.PressureBehavior](nsevent/pressurebehavior-swift.enum.md)
  These constants describe the behavior and progression of a pressure gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/pressurebehavior-swift.property)*