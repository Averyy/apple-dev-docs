# localTransform(atTime:)

**Framework**: Model I/O  
**Kind**: method

Returns the local transform matrix as of the specified time sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func localTransform(atTime time: TimeInterval) -> matrix_float4x4
```

#### Return Value

The local transformation matrix for the specified time sample.

#### Discussion

This matrix defines the position, orientation, shear, and scale for any object affected by the transform component, relative to the coordinate space of its parent, as of the specified time sample.

Requesting a sample outside the time range clamps returned values using the [`minimumTime`](mdltransformcomponent/minimumtime.md) and [`maximumTime`](mdltransformcomponent/maximumtime.md) properties. Some asset formats support continuous sampling, with interpolation for times between the samples stored in the asset; others are discrete. For an asset with discrete time information, requesting a sample time in between the samples stored in the asset returns data for the immediately preceding time.

## Parameters

- `time`: The time sample for which to request information.

## See Also

- [var minimumTime: TimeInterval](mdltransformcomponent/minimumtime.md)
  The timestamp for the first timed data sample in the transform component.
- [var maximumTime: TimeInterval](mdltransformcomponent/maximumtime.md)
  The timestamp for the last timed data sample in the transform component.
- [func setLocalTransform(matrix_float4x4, forTime: TimeInterval)](mdltransformcomponent/setlocaltransform(_:fortime:).md)
  Sets a new local transform matrix for the specified time sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformcomponent/localtransform(attime:))*