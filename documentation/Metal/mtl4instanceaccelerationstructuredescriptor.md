# MTL4InstanceAccelerationStructureDescriptor

**Framework**: Metal  
**Kind**: class

Descriptor for an instance acceleration structure.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4InstanceAccelerationStructureDescriptor
```

#### Overview

An instance acceleration structure references other acceleration structures, and provides the ability to “instantiate” them multiple times, each one with potentially a different transformation matrix.

You specify the properties of the instances in the acceleration structure this descriptor builds by providing a buffer of `structs` via its [`instanceDescriptorBuffer`](mtl4instanceaccelerationstructuredescriptor/instancedescriptorbuffer.md) property.

Use a [`MTLResidencySet`](mtlresidencyset.md) to mark residency of all buffers and acceleration structures this descriptor references when you build this acceleration structure.

## Topics

### Instance Properties
- [var instanceCount: Int](mtl4instanceaccelerationstructuredescriptor/instancecount.md)
  Controls the number of instance descriptors in the instance descriptor buffer references.
- [var instanceDescriptorBuffer: MTL4BufferRange](mtl4instanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
  Assigns a reference to a buffer containing instance descriptors for acceleration structures to reference.
- [var instanceDescriptorStride: Int](mtl4instanceaccelerationstructuredescriptor/instancedescriptorstride.md)
  Sets the stride, in bytes, between instance descriptors the instance descriptor buffer references.
- [var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType](mtl4instanceaccelerationstructuredescriptor/instancedescriptortype.md)
  Sets the type of instance descriptor that the instance descriptor buffer references.
- [var instanceTransformationMatrixLayout: MTLMatrixLayout](mtl4instanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.md)
  Specifies the layout for the transformation matrices in the instance descriptor buffer and the motion transformation matrix buffer.
- [var motionTransformBuffer: MTL4BufferRange](mtl4instanceaccelerationstructuredescriptor/motiontransformbuffer.md)
  A buffer containing transformation information for instance motion keyframes, formatted according to the motion transform type.
- [var motionTransformCount: Int](mtl4instanceaccelerationstructuredescriptor/motiontransformcount.md)
  Controls the total number of motion transforms in the motion transform buffer.
- [var motionTransformStride: Int](mtl4instanceaccelerationstructuredescriptor/motiontransformstride.md)
  Specify the stride for motion transform.
- [var motionTransformType: MTLTransformType](mtl4instanceaccelerationstructuredescriptor/motiontransformtype.md)
  Controls the type of motion transforms, either as a matrix or individual components.

## Relationships

### Inherits From
- [MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)
  Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
- [protocol MTLAccelerationStructure](mtlaccelerationstructure.md)
  A collection of model data for GPU-accelerated intersection of rays with the model.
- [class MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md)
  Base class for Metal 4 acceleration structure descriptors.
- [class MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md)
  A base class for classes that define the configuration for a new acceleration structure.
- [class MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md)
  Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [class MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md)
  A description of an acceleration structure that contains geometry primitives.
- [class MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [protocol MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md)
  An object for encoding commands that build or refit acceleration structures.
- [struct MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md)
  Options that describe which tasks you can perform on an acceleration structure and how the system performs those tasks.
- [struct MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor)*