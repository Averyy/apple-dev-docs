# Ray Tracing with Acceleration Structures

**Framework**: Metal

Build a representation of your scene’s geometry using triangles and bounding volumes to quickly trace rays through the scene.

#### Overview

Ray tracing can improve your content’s realism by more accurately modeling the behavior of light than traditional rendering. You can also use ray tracing to implement similar techniques that rely on line-of-sight, such as sound obstruction or visually based AI functions.

To apply ray tracing in your app:

1. Create acceleration structures that represent objects in a scene.
2. Define a ray’s behavior when it collides into parts of an acceleration structure by creating either intersectors or intersection queries.
3. Generate rays into the scene from a new or existing shader.

An  uses a table of your intersection functions that define the custom behavior for each intersection type. An  returns to your calling function to handle the custom behavior for all intersection types.

Intersectors work with compute kernels on all GPUs, and with render shaders only on Apple silicon GPUs. Alternatively, your app can use intersection queries on non-Apple GPUs, or for porting code from other graphics APIs.

## Topics

### Ray Tracing Samples
- [Accelerating ray tracing using Metal](accelerating-ray-tracing-using-metal.md)
  Implement ray-traced rendering using GPU-based parallel processing.
- [Control the Ray Tracing Process Using Intersection Queries](control-the-ray-tracing-process-using-intersection-queries.md)
  Explicitly enumerate a ray’s intersections with acceleration structures by creating an intersection query object.
- [Rendering reflections in real time using ray tracing](rendering-reflections-in-real-time-using-ray-tracing.md)
  Implement realistic real-time lighting by dynamically generating reflection maps by encoding a ray-tracing compute pass.
- [Rendering a curve primitive in a ray tracing scene](rendering-a-curve-primitive-in-a-ray-tracing-scene.md)
  Implement ray traced rendering using GPU-based parallel processing.
### Acceleration Structures
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
- [class MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [protocol MTLAccelerationStructureCommandEncoder](mtlaccelerationstructurecommandencoder.md)
  An object for encoding commands that build or refit acceleration structures.
- [struct MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md)
  Options that describe which tasks you can perform on an acceleration structure and how the system performs those tasks.
- [struct MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)
### Acceleration Structures Passes
- [class MTLAccelerationStructurePassDescriptor](mtlaccelerationstructurepassdescriptor.md)
- [class MTLAccelerationStructurePassSampleBufferAttachmentDescriptor](mtlaccelerationstructurepasssamplebufferattachmentdescriptor.md)
- [class MTLAccelerationStructurePassSampleBufferAttachmentDescriptorArray](mtlaccelerationstructurepasssamplebufferattachmentdescriptorarray.md)
### Geometry Descriptors
- [class MTL4AccelerationStructureGeometryDescriptor](mtl4accelerationstructuregeometrydescriptor.md)
  Base class for all Metal 4 acceleration structure geometry descriptors.
- [class MTLAccelerationStructureGeometryDescriptor](mtlaccelerationstructuregeometrydescriptor.md)
  A base class for descriptors that contain geometry data to convert into a ray-tracing acceleration structure.
- [class MTL4AccelerationStructureTriangleGeometryDescriptor](mtl4accelerationstructuretrianglegeometrydescriptor.md)
  Describes triangle geometry suitable for ray tracing.
- [class MTLAccelerationStructureTriangleGeometryDescriptor](mtlaccelerationstructuretrianglegeometrydescriptor.md)
  A description of a list of triangle primitives to turn into an acceleration structure.
- [class MTL4AccelerationStructureCurveGeometryDescriptor](mtl4accelerationstructurecurvegeometrydescriptor.md)
  Describes curve geometry suitable for ray tracing.
- [class MTLAccelerationStructureCurveGeometryDescriptor](mtlaccelerationstructurecurvegeometrydescriptor.md)
- [enum MTLCurveType](mtlcurvetype.md)
- [enum MTLCurveBasis](mtlcurvebasis.md)
- [enum MTLCurveEndCaps](mtlcurveendcaps.md)
- [class MTL4AccelerationStructureBoundingBoxGeometryDescriptor](mtl4accelerationstructureboundingboxgeometrydescriptor.md)
  Describes bounding-box geometry suitable for ray tracing.
- [class MTLAccelerationStructureBoundingBoxGeometryDescriptor](mtlaccelerationstructureboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes to turn into an acceleration structure.
### Motion Geometry Descriptors
- [class MTL4AccelerationStructureMotionTriangleGeometryDescriptor](mtl4accelerationstructuremotiontrianglegeometrydescriptor.md)
  Describes motion triangle geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionTriangleGeometryDescriptor](mtlaccelerationstructuremotiontrianglegeometrydescriptor.md)
  A description of a list of triangle primitives, as motion keyframe data, to turn into an acceleration structure.
- [class MTL4AccelerationStructureMotionCurveGeometryDescriptor](mtl4accelerationstructuremotioncurvegeometrydescriptor.md)
  Describes motion curve geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionCurveGeometryDescriptor](mtlaccelerationstructuremotioncurvegeometrydescriptor.md)
- [class MTL4AccelerationStructureMotionBoundingBoxGeometryDescriptor](mtl4accelerationstructuremotionboundingboxgeometrydescriptor.md)
  Describes motion bounding box geometry, suitable for motion ray tracing.
- [class MTLAccelerationStructureMotionBoundingBoxGeometryDescriptor](mtlaccelerationstructuremotionboundingboxgeometrydescriptor.md)
  A description of a list of bounding boxes, as motion keyframe data, to turn into an acceleration structure.
- [class MTLMotionKeyframeData](mtlmotionkeyframedata.md)
  Geometry data for a specific keyframe to use in a moving object.
### Instance Descriptors
- [struct MTLAccelerationStructureInstanceDescriptor](mtlaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure.
- [struct MTLAccelerationStructureUserIDInstanceDescriptor](mtlaccelerationstructureuseridinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier for the instance.
- [struct MTLAccelerationStructureMotionInstanceDescriptor](mtlaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure, with the instance including a user identifier and motion data for the instance.
- [struct MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstanceoptions.md)
  Options for adjusting the behavior of an instanced acceleration structure.
- [class MTL4IndirectInstanceAccelerationStructureDescriptor](mtl4indirectinstanceaccelerationstructuredescriptor.md)
  Descriptor for an “indirect” instance acceleration structure that allows providing the instance count and motion transform count indirectly, through buffer references.
- [class MTLIndirectInstanceAccelerationStructureDescriptor](mtlindirectinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that Metal derives from instances of primitive acceleration structures that the GPU can populate.
- [struct MTLIndirectAccelerationStructureInstanceDescriptor](mtlindirectaccelerationstructureinstancedescriptor.md)
  A description of an instance in an instanced geometry acceleration structure that the GPU can populate.
- [struct MTLIndirectAccelerationStructureMotionInstanceDescriptor](mtlindirectaccelerationstructuremotioninstancedescriptor.md)
  A description of an instance in an acceleration structure that the GPU can populate, with motion data for the instance.
### Intersection Function Tables
- [protocol MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
- [class MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [class MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [struct MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature.md)
  Constants for specifying different types of custom intersection functions.
- [struct MTLIntersectionFunctionBufferArguments](mtlintersectionfunctionbufferarguments.md)
### Supporting Types
- [typealias MTLAxisAlignedBoundingBox](mtlaxisalignedboundingbox-swift.typealias.md)
  The bounds for an axis-aligned bounding box.
- [typealias MTLPackedFloat3](mtlpackedfloat3-swift.typealias.md)
  }
- [typealias MTLPackedFloat4x3](mtlpackedfloat4x3-swift.typealias.md)
  A structure that contains the top three rows of a 4x4 matrix of 32-bit floating-point values, in column-major order.
- [func MTLPackedFloat3Make(Float, Float, Float) -> MTLPackedFloat3](mtlpackedfloat3make(_:_:_:).md)
  Returns a new packed vector with three floating-point values.
- [struct MTL4BufferRange](mtl4bufferrange.md)
- [func MTL4BufferRangeMake(UInt64, UInt64) -> MTL4BufferRange](mtl4bufferrangemake(_:_:).md)

## See Also

- [Render Passes](render-passes.md)
  Encode a render pass to draw graphics into an image.
- [Compute Passes](compute-passes.md)
  Encode a compute pass that runs computations in parallel on a thread grid, processing and manipulating Metal resource data on multiple cores of a GPU.
- [Machine-Learning Passes](machine-learning-passes.md)
  Add machine-learning model inference to your Metal app’s GPU workflow.
- [Blit Passes](blit-passes.md)
  Encode a block information transfer pass to adjust and copy data to and from GPU resources, such as buffers and textures.
- [Indirect Command Encoding](indirect-command-encoding.md)
  Store draw commands in Metal buffers and run them at a later time on the GPU, either once or repeatedly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/ray-tracing-with-acceleration-structures)*