# init(stiffness:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an inflation configuration that defaults to the mesh volume.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(stiffness: Float = 1.0)
```

## Parameters

- `stiffness`: The resistance to diverge from the target volume. Valid range is [0.0, 1.0].

## See Also

### Creating an inflation constraint
- [init(targetVolume: Float, stiffness: Float)](./init%28targetvolume,stiffness%29.md)
  Creates an inflation configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothbodycomponent/inflationconstraint-swift.struct/init(stiffness:))*