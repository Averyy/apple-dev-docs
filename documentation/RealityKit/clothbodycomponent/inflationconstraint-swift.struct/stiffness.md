# stiffness

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The resistance of the body’s volume to diverge from `targetVolume`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var stiffness: Float { get set }
```

## Discussion

The valid range is [0.0, 1.0], both included.

## See Also

### Configuring inflation
- [var targetVolume: Float?](./targetvolume.md)
  The target volume (in ㎥) that the body tries to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/inflationconstraint-swift.struct/stiffness)*