# input

**Framework**: Game Controller  
**Kind**: property

Gets the input profile for the stylus.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var input: (any GCDevicePhysicalInput)? { get }
```

## Mentions

- [Discovering and tracking spatial game controllers and styli](discovering-and-tracking-spatial-game-controllers-and-styli.md)

#### Discussion

The input profile is represented as an object conforming to the `GCDevicePhysicalInput` protocol.  Use this object to discover available inputs on the stylus, including buttons and pressure sensors, and get notified when the state of those inputs change.

## See Also

- [var haptics: GCDeviceHaptics?](gcstylus/haptics.md)
  Gets the haptics profile for the stylus, if supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylus/input)*