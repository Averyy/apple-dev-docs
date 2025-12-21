# MTLAccelerationStructureUsage

**Framework**: Metal  
**Kind**: struct

Options that affect how Metal builds an acceleration structure and the behavior of that acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLAccelerationStructureUsage
```

## Topics

### Applying options
- [static var refit: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/refit.md)
  An option that lets you update an acceleration structure after creating it.
- [static var preferFastBuild: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/preferfastbuild.md)
  An option that instructs Metal to build an acceleration structure quickly.
- [static var preferFastIntersection: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/preferfastintersection.md)
  An option that instructs Metal to prioritize building an acceleration structure with better intersection performance.
- [static var minimizeMemory: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/minimizememory.md)
  An option that instructs Metal to prioritize building an acceleration structure that needs less memory.
- [static var extendedLimits: MTLAccelerationStructureUsage](mtlaccelerationstructureusage/extendedlimits.md)
  An option that increases an acceleration structure’s storage capacity.
### Swift support
- [init(rawValue: UInt)](mtlaccelerationstructureusage/init(rawvalue:).md)
  Creates new usage options instance from a raw integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Improving ray-tracing data access using per-primitive data](improving-ray-tracing-data-access-using-per-primitive-data.md)
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
- [class MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [protocol MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md)
  Encodes commands that build and refit acceleration structures for a single pass.
- [struct MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureusage)*