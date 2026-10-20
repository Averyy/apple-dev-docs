# acceleratorPedal

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The controller’s accelerator pedal element.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
var acceleratorPedal: (any GCButtonElement)? { get }
```

```objc
@property (readonly, nullable) id<GCButtonElement> acceleratorPedal;
```

## See Also

### Getting input elements
- [var wheel: GCSteeringWheelElement](./wheel.md)
  The controller’s wheel element.
- [var brakePedal: (any GCButtonElement)?](./brakepedal.md)
  The controller’s brake pedal element.
- [var clutchPedal: (any GCButtonElement)?](./clutchpedal.md)
  The controller’s clutch element.
- [var shifter: GCGearShifterElement?](./shifter.md)
  The controller’s gear shift element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheelinputstate/acceleratorpedal)*