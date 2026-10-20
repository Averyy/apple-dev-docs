# brakePedal

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The controller’s brake pedal element.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
var brakePedal: (any GCButtonElement)? { get }
```

```objc
@property (readonly, nullable) id<GCButtonElement> brakePedal;
```

## See Also

### Getting input elements
- [var wheel: GCSteeringWheelElement](./wheel.md)
  The controller’s wheel element.
- [var acceleratorPedal: (any GCButtonElement)?](./acceleratorpedal.md)
  The controller’s accelerator pedal element.
- [var clutchPedal: (any GCButtonElement)?](./clutchpedal.md)
  The controller’s clutch element.
- [var shifter: GCGearShifterElement?](./shifter.md)
  The controller’s gear shift element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheelinputstate/brakepedal)*