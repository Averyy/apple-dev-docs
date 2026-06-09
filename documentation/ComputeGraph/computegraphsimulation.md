# ComputeGraphSimulation

**Framework**: ComputeGraph  
**Kind**: class

A simulation of particles, which use a single pipeline.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
final class ComputeGraphSimulation
```

#### Overview

This class is independent of the output, which makes for simpler testing.

## Topics

### Structures
- [ComputeGraphSimulation.AdvanceParams](computegraphsimulation/advanceparams.md)
  Parameters for advancing a compute graph simulation by one time step.
- [ComputeGraphSimulation.SimulationRate](computegraphsimulation/simulationrate-swift.struct.md)
  Specifies the rate and mode for simulation.
### Initializers
- [convenience init(pipelines: ComputeNodeGraph.Pipelines?)](computegraphsimulation/init(pipelines:).md)
  Initialize a ComputeGraphSimulation for the given pipelines, or a default pipeline if not specified.
- [convenience init(pipelines: ComputeNodeGraph.Pipelines, commandQueue: any MTLCommandQueue)](computegraphsimulation/init(pipelines:commandqueue:).md)
  Initialize a ComputeGraphSimulation for the given pipelines
### Instance Properties
- [var commandQueue: any MTLCommandQueue](computegraphsimulation/commandqueue.md)
- [var graphParametersBuffer: (any MTLBuffer)!](computegraphsimulation/graphparametersbuffer.md)
- [var graphUniforms: any MTLBuffer](computegraphsimulation/graphuniforms.md)
  Returns a read-only copy of the uniforms buffer.
- [var outputIds: [Int]](computegraphsimulation/outputids.md)
- [var pipelines: ComputeNodeGraph.Pipelines](computegraphsimulation/pipelines.md)
- [var simulationRate: ComputeGraphSimulation.SimulationRate](computegraphsimulation/simulationrate-swift.property.md)
  Specifies the current simulation rate.
### Instance Methods
- [func addUserResource(any MTLResource)](computegraphsimulation/adduserresource(_:).md)
  Registers a resource for residency on all command encoders used by this simulation.
- [func advance(ComputeGraphSimulation.AdvanceParams)](computegraphsimulation/advance(_:).md)
  Advances the simulation by one time step, encoding all simulation stage dispatches into the command buffer and encoder provided by `params`.
- [func buffer(at: Int) -> (any MTLBuffer, bufferOffset: Int)?](computegraphsimulation/buffer(at:).md)
- [func fastForward()](computegraphsimulation/fastforward.md)
- [func fastForward(stepCount: Int, stepDeltaTime: Float)](computegraphsimulation/fastforward(stepcount:stepdeltatime:).md)
  Advances the particle simulation by multiple steps in a single operation.
- [func isOutputEnabled(Int) -> Bool](computegraphsimulation/isoutputenabled(_:).md)
  Returns whether the specified output is currently enabled for simulation.
- [func modifyUniforms<E, R>((UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R](computegraphsimulation/modifyuniforms(_:).md)
  Provides read/write access to the entire uniforms buffer for CPU access.
- [func reset(encoder: any MTLComputeCommandEncoder)](computegraphsimulation/reset(encoder:).md)
  Resets the simulation to its initial state, clearing all live elements and accumulated time.
- [func resetRandomSeeds(using: () -> UInt32)](computegraphsimulation/resetrandomseeds(using:).md)
  Resets random seeds using the provided randomness function.
- [func setBuffer((any MTLBuffer)?, bufferOffset: Int, at: ComputeNodeGraph.Assembly.Location)](computegraphsimulation/setbuffer(_:bufferoffset:at:)-772ch.md)
- [func setBuffer((any MTLBuffer)?, bufferOffset: Int, at: Int)](computegraphsimulation/setbuffer(_:bufferoffset:at:)-bmmd.md)
- [func setBuffer(any MTLBuffer, bufferOffset: Int, elementCount: Int, at: ComputeNodeGraph.Assembly.Location)](computegraphsimulation/setbuffer(_:bufferoffset:elementcount:at:).md)
- [func setBuffers([(any MTLBuffer)?], bufferOffsets: [Int]?)](computegraphsimulation/setbuffers(_:bufferoffsets:).md)
- [func setOutputEnabled(Int, enabled: Bool)](computegraphsimulation/setoutputenabled(_:enabled:).md)
  Enables or disables execution of the provided output stage, without disabling the system it represents.
- [func setTexture((any MTLTexture)?, at: Int)](computegraphsimulation/settexture(_:at:).md)
  Binds a Metal texture to the texture slot at the given index.
- [func setTextures([(any MTLTexture)?])](computegraphsimulation/settextures(_:).md)
- [func setUniform<V>(V, named: String) -> Bool](computegraphsimulation/setuniform(_:named:).md)
  Finds the named uniform and sets it to the given BitwiseCopyable value.
- [func setUniformData(Data, at: ComputeNodeGraph.Assembly.Location)](computegraphsimulation/setuniformdata(_:at:).md)
- [func setUniformValue<V>(V, at: ComputeNodeGraph.Assembly.Location)](computegraphsimulation/setuniformvalue(_:at:).md)
  Copies the contents of `value` into the location specified by `relocation`
- [func setUserResources([any MTLResource])](computegraphsimulation/setuserresources(_:).md)
  Sets additional resources for residency on all command buffers used by this simulation, replacing any previously added resources.
- [func spawn(elements: borrowing [ElementSpawnParameters], in: Int?, using: any MTLComputeCommandEncoder)](computegraphsimulation/spawn(elements:in:using:).md)
  Spawns new elements into the simulation with the given initial parameters.
- [func texture(at: Int) -> (any MTLTexture)?](computegraphsimulation/texture(at:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation)*