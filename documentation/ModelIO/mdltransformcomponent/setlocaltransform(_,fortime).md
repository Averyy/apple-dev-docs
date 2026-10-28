# setLocalTransform(_:forTime:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setLocalTransform:(matrix_float4x4) transform forTime:(NSTimeInterval) time;
```

## Discussion

Calling this method updates the [`minimumTime`](./minimumtime.md) and [`maximumTime`](./maximumtime.md) properties to reflect the range of sample values stored in the transform component.

## Parameters

- `transform`: The local transformation matrix for the specified time sample.
- `time`: The time sample with which to associate transform information.

## See Also

### Working with Animated Transforms
- [var minimumTime: TimeInterval](./minimumtime.md)
  The timestamp for the first timed data sample in the transform component.
- [var maximumTime: TimeInterval](./maximumtime.md)
  The timestamp for the last timed data sample in the transform component.
- [func localTransform(atTime: TimeInterval) -> matrix_float4x4](./localtransform%28attime%29.md)
  Returns the local transform matrix as of the specified time sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformcomponent/setlocaltransform(_:fortime:))*