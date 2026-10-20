# instanceTransformationMatrixLayout

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Specifies the layout for the transformation matrices in the instance descriptor buffer and the motion transformation matrix buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var instanceTransformationMatrixLayout: MTLMatrixLayout { get set }
```

```objc
@property (nonatomic) MTLMatrixLayout instanceTransformationMatrixLayout;
```

#### Discussion

Metal interprets the value of this property as the layout for the buffers that both [`instanceDescriptorBuffer`](./instancedescriptorbuffer.md) and [`motionTransformBuffer`](./motiontransformbuffer.md) reference.

Defaults to `MTLMatrixLayoutColumnMajor`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancetransformationmatrixlayout)*