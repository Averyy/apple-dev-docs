# vertexBuffers

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array of motion keyframes, each containing triangle data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var vertexBuffers: [MTLMotionKeyframeData] { get set }
```

```objc
@property (nonatomic, copy) NSArray<MTLMotionKeyframeData *> * vertexBuffers;
```

## See Also

### Specifying vertex data
- [var vertexStride: Int](./vertexstride.md)
  The stride, in bytes, between vertices in each vertex buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotiontrianglegeometrydescriptor/vertexbuffers)*