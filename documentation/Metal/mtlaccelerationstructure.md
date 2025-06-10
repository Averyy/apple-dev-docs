# MTLAccelerationStructure

**Framework**: Metal  
**Kind**: protocol

A collection of model data for GPU-accelerated intersection of rays with the model.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLAccelerationStructure : MTLResource
```

## Mentions

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Overview

To accelerate ray tracing, the device object needs to reorganize your model data into an optimized data structure for intersection testing on that GPU. Create  [`MTLAccelerationStructure`](mtlaccelerationstructure.md) objects to contain your model data and reference them in compute and render  commands that execute ray-tracing operations.

You don’t define classes that implement this protocol. To create an acceleration structure, you create a descriptor object and configure its properties with your model data. Then call the [`makeAccelerationStructure(descriptor:)`](mtldevice/makeaccelerationstructure(descriptor:).md) method on the Metal device object to create the object and reserve memory for the structure. To populate the structure with the data, use a [`MTLAccelerationStructureCommandEncoder`](mtlaccelerationstructurecommandencoder.md) to encode GPU commands.

Metal provides multiple descriptor classes, each describing a different type of model data. Choose the appropriate descriptor for each acceleration structure you want to make. Most often, you create an acceleration structure for each list of triangles or bounding boxes. Then collect related geometry structures into a primitive acceleration structure. Create instance acceleration structures when you need to reference instances of primitive acceleration structures at different locations within a scene.

The table below summarizes the descriptor classes:

| Descriptor class | Usage |
| --- | --- |
| [`MTLAccelerationStructureTriangleGeometryDescriptor`](mtlaccelerationstructuretrianglegeometrydescriptor.md) | Describes an acceleration structure for a list of triangles. |
| [`MTLAccelerationStructureBoundingBoxGeometryDescriptor`](mtlaccelerationstructureboundingboxgeometrydescriptor.md) | Describes an acceleration structure for a list of bounding boxes. |
| [`MTLPrimitiveAccelerationStructureDescriptor`](mtlprimitiveaccelerationstructuredescriptor.md) | Describes an acceleration structure for a list of bounding-box or triangle acceleration structures, effectively creating a union of all of the underlying geometry. |
| [`MTLInstanceAccelerationStructureDescriptor`](mtlinstanceaccelerationstructuredescriptor.md) | Describes an acceleration structure for a list of instances of primitive acceleration structures. |

## Topics

### Reading the Structure’s Size
- [var size: Int](mtlaccelerationstructure/size.md)
  The size of the acceleration structure’s memory allocation, in bytes.
### Instance Properties
- [var gpuResourceID: MTLResourceID](mtlaccelerationstructure/gpuresourceid.md)

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [MTLResource](mtlresource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)
  Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
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
- [class MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [protocol MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md)
  An object for encoding commands that build or refit acceleration structures.
- [struct MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md)
  Options that describe which tasks you can perform on an acceleration structure and how the system performs those tasks.
- [struct MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructure)*