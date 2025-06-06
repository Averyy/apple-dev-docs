# BillboardAction.Transition

**Framework**: RealityKit  
**Kind**: struct

The duration and timing of how an action event transitions from one state to another.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Transition
```

## Topics

### Initializers
- [init(duration: TimeInterval, timingFunction: AnimationTimingFunction)](billboardaction/transition/init(duration:timingfunction:).md)
  Creates a transition with a duration and timing function.
- [init(from: any Decoder) throws](billboardaction/transition/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var duration: TimeInterval](billboardaction/transition/duration.md)
  The amount of time the transition takes to go from one state to another.
- [var timingFunction: AnimationTimingFunction](billboardaction/transition/timingfunction.md)
  The rate of change at the beginning and end of the transition.
### Instance Methods
- [func encode(to: any Encoder) throws](billboardaction/transition/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/billboardaction/transition)*