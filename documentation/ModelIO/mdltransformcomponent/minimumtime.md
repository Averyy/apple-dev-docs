# minimumTime

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The timestamp for the first timed data sample in the transform component.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var minimumTime: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval minimumTime;
```

## Discussion

Timed data is clamped to the minimum and maximum times. If you request transform data for a time sample before the minimum time, Model I/O returns the transform at the minimum time.

If the transform component does not contain timed information, this property’s value is zero.

## See Also

### Working with Animated Transforms
- [var maximumTime: TimeInterval](./maximumtime.md)
  The timestamp for the last timed data sample in the transform component.
- [func localTransform(atTime: TimeInterval) -> matrix_float4x4](./localtransform%28attime%29.md)
  Returns the local transform matrix as of the specified time sample.
- [func setLocalTransform(matrix_float4x4, forTime: TimeInterval)](./setlocaltransform%28_,fortime%29.md)
  Sets a new local transform matrix for the specified time sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdltransformcomponent/minimumtime)*