# matrix

**Framework**: Model I/O  
**Kind**: property  
**Required**: Yes

The transform matrix that defines the local coordinate space relative to a parent coordinate space.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var matrix: matrix_float4x4 { get set }
```

#### Discussion

This matrix defines the position, orientation, shear, and scale for any object affected by the transform component, relative to the coordinate space of its parent.

If the transform component includes time-based transform information, this method returns the local transform matrix as of the earliest time sample (as reported by the [`minimumTime`](mdltransformcomponent/minimumtime.md) property).

## See Also

- [func setLocalTransform(matrix_float4x4)](mdltransformcomponent/setlocaltransform(_:).md)
  Sets a new static transform matrix, overriding any time-based transform information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformcomponent/matrix)*