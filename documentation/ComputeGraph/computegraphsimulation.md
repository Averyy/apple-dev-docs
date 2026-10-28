# ComputeGraphSimulation

**Framework**: Compute Graph  
**Kind**: class  
**Role**: Class

A simulation of particles, which use a single pipeline.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
final class ComputeGraphSimulation
```

## Overview

This class is independent of the output, which makes for simpler testing.

## Topics

### Structures
- [ComputeGraphSimulation.AdvanceParams](./computegraphsimulation/advanceparams.md)
  Parameters for advancing a compute graph simulation by one time step.
- [ComputeGraphSimulation.SimulationRate](./computegraphsimulation/simulationrate-swift.struct.md)
  Specifies the rate and mode for simulation.
### Initializers
- [convenience init(pipelines: ComputeNodeGraph.Pipelines?)](./computegraphsimulation/init%28pipelines%29.md)
  Initialize a ComputeGraphSimulation for the given pipelines, or a default pipeline if not specified.
- [convenience init(pipelines: ComputeNodeGraph.Pipelines, commandQueue: any MTLCommandQueue)](./computegraphsimulation/init%28pipelines,commandqueue%29.md)
  Initialize a ComputeGraphSimulation for the given pipelines
### Instance Properties
- [var commandQueue: any MTLCommandQueue](./computegraphsimulation/commandqueue.md)
- [var graphUniforms: any MTLBuffer](./computegraphsimulation/graphuniforms.md)
  Returns a read-only copy of the uniforms buffer.
- [var pipelines: ComputeNodeGraph.Pipelines](./computegraphsimulation/pipelines.md)
- [var simulationRate: ComputeGraphSimulation.SimulationRate](./computegraphsimulation/simulationrate-swift.property.md)
  Specifies the current simulation rate.
### Instance Methods
- [func addUserResource(any MTLResource)](./computegraphsimulation/adduserresource%28_%29.md)
  Registers a resource for residency on all command encoders used by this simulation.
- [func advance(ComputeGraphSimulation.AdvanceParams)](./computegraphsimulation/advance%28_%29.md)
  Advances the simulation by one time step, encoding all simulation stage dispatches into the command buffer and encoder provided by `params`.
- [func buffer(at: Int) -> (any MTLBuffer, bufferOffset: Int)?](./computegraphsimulation/buffer%28at%29.md)
- [func fastForward()](./computegraphsimulation/fastforward%28%29.md)
- [func fastForward(stepCount: Int, stepDeltaTime: Float)](./computegraphsimulation/fastforward%28stepcount,stepdeltatime%29.md)
  Advances the particle simulation by multiple steps in a single operation.
- [func isOutputEnabled(Int) -> Bool](./computegraphsimulation/isoutputenabled%28_%29.md)
  Returns whether the specified output is currently enabled for simulation.
- [func modifyUniforms<E, R>((UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R](./computegraphsimulation/modifyuniforms%28_%29.md)
  Provides read/write access to the entire uniforms buffer for CPU access.
- [func reset(encoder: any MTLComputeCommandEncoder)](./computegraphsimulation/reset%28encoder%29.md)
  Resets the simulation to its initial state, clearing all live elements and accumulated time.
- [func resetRandomSeeds(using: () -> UInt32)](./computegraphsimulation/resetrandomseeds%28using%29.md)
  Resets random seeds using the provided randomness function.
- [func setBuffer((any MTLBuffer)?, bufferOffset: Int, at: ComputeNodeGraph.Assembly.Location)](./computegraphsimulation/setbuffer%28_,bufferoffset,at%29-772ch.md)
- [func setBuffer((any MTLBuffer)?, bufferOffset: Int, at: Int)](./computegraphsimulation/setbuffer%28_,bufferoffset,at%29-bmmd.md)
- [func setBuffer(any MTLBuffer, bufferOffset: Int, elementCount: Int, at: ComputeNodeGraph.Assembly.Location)](./computegraphsimulation/setbuffer%28_,bufferoffset,elementcount,at%29.md)
- [func setBuffers([(any MTLBuffer)?], bufferOffsets: [Int]?)](./computegraphsimulation/setbuffers%28_,bufferoffsets%29.md)
- [func setOutputEnabled(Int, enabled: Bool)](./computegraphsimulation/setoutputenabled%28_,enabled%29.md)
  Enables or disables execution of the provided output stage, without disabling the system it represents.
- [func setTexture((any MTLTexture)?, at: Int)](./computegraphsimulation/settexture%28_,at%29.md)
  Binds a Metal texture to the texture slot at the given index.
- [func setTextures([(any MTLTexture)?])](./computegraphsimulation/settextures%28_%29.md)
- [func setUniform<V>(V, named: String) -> Bool](./computegraphsimulation/setuniform%28_,named%29.md)
  Finds the named uniform and sets it to the given BitwiseCopyable value.
- [func setUniformData(Data, at: ComputeNodeGraph.Assembly.Location)](./computegraphsimulation/setuniformdata%28_,at%29.md)
- [func setUniformValue<V>(V, at: ComputeNodeGraph.Assembly.Location)](./computegraphsimulation/setuniformvalue%28_,at%29.md)
  Copies the contents of `value` into the location specified by `relocation`
- [func setUserResources([any MTLResource])](./computegraphsimulation/setuserresources%28_%29.md)
  Sets additional resources for residency on all command buffers used by this simulation, replacing any previously added resources.
- [func spawn(elements: borrowing [ElementSpawnParameters], in: Int?, using: any MTLComputeCommandEncoder)](./computegraphsimulation/spawn%28elements,in,using%29.md)
  Spawns new elements into the simulation with the given initial parameters.
- [func texture(at: Int) -> (any MTLTexture)?](./computegraphsimulation/texture%28at%29.md)

## See Also

### Running a simulation
- [struct ElementSpawnParameters](./elementspawnparameters.md)
  Parameters used to configure the initial state of a particle when it’s spawned in the simulation.
- [enum ElementGrouping](./elementgrouping.md)
  An enumeration of how elements are grouped.
- [ComputeGraphSimulation.SimulationRate](./computegraphsimulation/simulationrate-swift.struct.md)
  Specifies the rate and mode for simulation.
- [enum Sorting](./sorting.md)
  An enumeration of sorting modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation)*