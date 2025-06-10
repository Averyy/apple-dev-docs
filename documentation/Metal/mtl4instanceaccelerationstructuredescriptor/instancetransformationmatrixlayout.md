# instanceTransformationMatrixLayout

**Framework**: Metal  
**Kind**: property

Specifies the layout for the transformation matrices in the instance descriptor buffer and the motion transformation matrix buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var instanceTransformationMatrixLayout: MTLMatrixLayout { get set }
```

#### Discussion

Metal interprets the value of this property as the layout for the buffers that both [`instanceDescriptorBuffer`](mtl4instanceaccelerationstructuredescriptor/instancedescriptorbuffer.md) and [`motionTransformBuffer`](mtl4instanceaccelerationstructuredescriptor/motiontransformbuffer.md) reference.

Defaults to `MTLMatrixLayoutColumnMajor`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor/instancetransformationmatrixlayout)*