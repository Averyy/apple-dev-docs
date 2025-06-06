# maximumTime

**Framework**: Model I/O  
**Kind**: property  
**Required**: Yes

The timestamp for the last timed data sample in the transform component.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var maximumTime: TimeInterval { get }
```

#### Discussion

Timed data is clamped to the minimum and maximum times. If you request transform data for a time sample after the maximum time, Model I/O returns the transform at the maximum time.

If the transform component does not contain timed information, this property’s value is zero.

## See Also

- [var minimumTime: TimeInterval](mdltransformcomponent/minimumtime.md)
  The timestamp for the first timed data sample in the transform component.
- [func localTransform(atTime: TimeInterval) -> matrix_float4x4](mdltransformcomponent/localtransform(attime:).md)
  Returns the local transform matrix as of the specified time sample.
- [func setLocalTransform(matrix_float4x4, forTime: TimeInterval)](mdltransformcomponent/setlocaltransform(_:fortime:).md)
  Sets a new local transform matrix for the specified time sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformcomponent/maximumtime)*