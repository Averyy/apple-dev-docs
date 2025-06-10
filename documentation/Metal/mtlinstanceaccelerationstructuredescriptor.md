# MTLInstanceAccelerationStructureDescriptor

**Framework**: Metal  
**Kind**: class

A description of an acceleration structure that derives from instances of primitive acceleration structures.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLInstanceAccelerationStructureDescriptor
```

#### Overview

Metal provides acceleration structures with a two-level hierarchy. The bottom layer consists of primitive acceleration structures, which instance acceleration structures in the top level reference.

## Topics

### Specifying the Instance Structures
- [var instanceDescriptorType: MTLAccelerationStructureInstanceDescriptorType](mtlinstanceaccelerationstructuredescriptor/instancedescriptortype.md)
  The format of the instance data in the descriptor buffer.
- [var instancedAccelerationStructures: [any MTLAccelerationStructure]?](mtlinstanceaccelerationstructuredescriptor/instancedaccelerationstructures.md)
  The bottom-level acceleration structures that instances use in the instance acceleration structure .
- [enum MTLAccelerationStructureInstanceDescriptorType](mtlaccelerationstructureinstancedescriptortype.md)
  Options for specifying different kinds of instance types.
### Specifying the List of Instances
- [var instanceCount: Int](mtlinstanceaccelerationstructuredescriptor/instancecount.md)
  The number of instances in the instance descriptor buffer.
- [var instanceDescriptorBuffer: (any MTLBuffer)?](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbuffer.md)
  A buffer that contains descriptions of each instance in the acceleration structure.
- [var instanceDescriptorBufferOffset: Int](mtlinstanceaccelerationstructuredescriptor/instancedescriptorbufferoffset.md)
  The offset, in bytes, to the descripton of the first instance.
- [var instanceDescriptorStride: Int](mtlinstanceaccelerationstructuredescriptor/instancedescriptorstride.md)
  The stride, in bytes, between instance descriptions.
### Specifying Motion Data
- [var motionTransformCount: Int](mtlinstanceaccelerationstructuredescriptor/motiontransformcount.md)
  The number of motion transforms in the motion transform buffer.
- [var motionTransformBuffer: (any MTLBuffer)?](mtlinstanceaccelerationstructuredescriptor/motiontransformbuffer.md)
  A buffer that contains descriptions of each motion transform in the acceleration structure.
- [var motionTransformBufferOffset: Int](mtlinstanceaccelerationstructuredescriptor/motiontransformbufferoffset.md)
  The offset, in bytes, to the descripton of the first motion transform.
### Instance Properties
- [var instanceTransformationMatrixLayout: MTLMatrixLayout](mtlinstanceaccelerationstructuredescriptor/instancetransformationmatrixlayout.md)
- [var motionTransformStride: Int](mtlinstanceaccelerationstructuredescriptor/motiontransformstride.md)
- [var motionTransformType: MTLTransformType](mtlinstanceaccelerationstructuredescriptor/motiontransformtype.md)

## Relationships

### Inherits From
- [MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md)
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
- [class MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md)
  Descriptor for an instance acceleration structure.
- [protocol MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md)
  An object for encoding commands that build or refit acceleration structures.
- [struct MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md)
  Options that describe which tasks you can perform on an acceleration structure and how the system performs those tasks.
- [struct MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlinstanceaccelerationstructuredescriptor)*