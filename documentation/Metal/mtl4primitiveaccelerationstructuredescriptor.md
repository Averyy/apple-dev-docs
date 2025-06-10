# MTL4PrimitiveAccelerationStructureDescriptor

**Framework**: Metal  
**Kind**: class

Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4PrimitiveAccelerationStructureDescriptor
```

## Topics

### Instance Properties
- [var geometryDescriptors: [MTL4AccelerationStructureGeometryDescriptor]?](mtl4primitiveaccelerationstructuredescriptor/geometrydescriptors.md)
  Associates the array of geometry descriptors that comprise this primitive acceleration structure.
- [var motionEndBorderMode: MTLMotionBorderMode](mtl4primitiveaccelerationstructuredescriptor/motionendbordermode.md)
  Configures the motion border mode.
- [var motionEndTime: Float](mtl4primitiveaccelerationstructuredescriptor/motionendtime.md)
  Configures the motion end time for this geometry.
- [var motionKeyframeCount: Int](mtl4primitiveaccelerationstructuredescriptor/motionkeyframecount.md)
  Sets the motion keyframe count.
- [var motionStartBorderMode: MTLMotionBorderMode](mtl4primitiveaccelerationstructuredescriptor/motionstartbordermode.md)
  Configures the behavior when the ray-tracing system samples the acceleration structure before the motion start time.
- [var motionStartTime: Float](mtl4primitiveaccelerationstructuredescriptor/motionstarttime.md)
  Configures the motion start time for this geometry.

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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4primitiveaccelerationstructuredescriptor)*