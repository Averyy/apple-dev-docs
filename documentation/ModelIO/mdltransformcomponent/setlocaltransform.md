# setLocalTransform(_:)

**Framework**: Model I/O  
**Kind**: method

Sets a new static transform matrix, overriding any time-based transform information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func setLocalTransform(_ transform: matrix_float4x4)
```

#### Discussion

Calling this method sets both the [`minimumTime`](mdltransformcomponent/minimumtime.md) and [`maximumTime`](mdltransformcomponent/maximumtime.md) properties to zero.

## Parameters

- `transform`: A new static transform matrix.

## See Also

- [var matrix: matrix_float4x4](mdltransformcomponent/matrix.md)
  The transform matrix that defines the local coordinate space relative to a parent coordinate space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformcomponent/setlocaltransform(_:))*