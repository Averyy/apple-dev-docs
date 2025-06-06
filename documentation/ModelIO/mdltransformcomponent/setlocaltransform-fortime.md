# setLocalTransform(_:forTime:)

**Framework**: Model I/O  
**Kind**: method

Sets a new local transform matrix for the specified time sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func setLocalTransform(_ transform: matrix_float4x4, forTime time: TimeInterval)
```

#### Discussion

Calling this method updates the [`minimumTime`](mdltransformcomponent/minimumtime.md) and [`maximumTime`](mdltransformcomponent/maximumtime.md) properties to reflect the range of sample values stored in the transform component.

## Parameters

- `transform`: The local transformation matrix for the specified time sample.
- `time`: The time sample with which to associate transform information.

## See Also

- [var minimumTime: TimeInterval](mdltransformcomponent/minimumtime.md)
  The timestamp for the first timed data sample in the transform component.
- [var maximumTime: TimeInterval](mdltransformcomponent/maximumtime.md)
  The timestamp for the last timed data sample in the transform component.
- [func localTransform(atTime: TimeInterval) -> matrix_float4x4](mdltransformcomponent/localtransform(attime:).md)
  Returns the local transform matrix as of the specified time sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformcomponent/setlocaltransform(_:fortime:))*