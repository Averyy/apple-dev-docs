# Compute Graph

**Framework**: Compute Graph  
**Kind**: module

Build and run custom particle effects and compute simulations for RealityKit using a programmable node graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro 3.0+

#### Overview

Compute Graph is a node-based framework for building particle simulations and general-purpose GPU compute graphs in [`RealityKit`](https://developer.apple.com/documentation/realitykit). Where [`ShaderGraph`](https://developer.apple.com/documentation/shadergraph) lets you build material appearance through a node-based visual editor, Compute Graph provides the same graph-driven, connection-based authoring for simulation behavior. Use Compute Graph when you build tools or editors that need fine-grained, per-stage control over how simulations execute on the GPU. Reality Composer Pro uses this framework to author and preview particle systems for RealityKit scenes.

The Swift API centers on a three-step compilation pipeline. Describe a simulation as a [`ComputeNodeGraph`](computenodegraph.md), a directed graph of typed nodes and edges. Then produce a [`ComputeNodeGraph.Assembly`](computenodegraph/assembly.md) from the graph, which resolves the buffer, uniform, and texture layout the simulation requires. Compile that assembly into [`ComputeNodeGraph.Pipelines`](computenodegraph/pipelines.md) to produce GPU shader code; a single set of pipelines can back multiple [`ComputeGraphSimulation`](computegraphsimulation.md) instances running concurrently. Supply custom Metal Shading Language functions through a [`ComputeNodeGraph.Library`](computenodegraph/library.md) alongside the framework’s built-in node namespaces.

At runtime, [`ComputeGraphSimulation`](computegraphsimulation.md) drives GPU execution. Call [`advance(_:)`](computegraphsimulation/advance(_:).md) each frame, passing a [`ComputeGraphSimulation.AdvanceParams`](computegraphsimulation/advanceparams.md) that carries the time delta, a Metal command buffer, a compute encoder, and optional world-space transforms. To inject elements programmatically, call [`spawn(elements:in:using:)`](computegraphsimulation/spawn(elements:in:using:).md) with [`ElementSpawnParameters`](elementspawnparameters.md) values that set each element’s initial position, velocity, size, color, and lifetime.

## Topics

### Graph definition and assembly
- [struct ComputeNodeGraph](computenodegraph.md)
- [ComputeNodeGraph.Assembly](computenodegraph/assembly.md)
  Fully assembled configuration of compute graph nodes.
- [ComputeNodeGraph.Pipelines](computenodegraph/pipelines.md)
  Fully-compiled shaders for a compute graph.
- [ComputeNodeGraph.PipelinesDescriptor](computenodegraph/pipelinesdescriptor.md)
  Specifies the configuration used to compile a set of compute pipelines for a compute graph effect.
- [ComputeNodeGraph.NodeDefinition](computenodegraph/nodedefinition.md)
- [ComputeNodeGraph.Library](computenodegraph/library.md)
  A class defining a library of node definitions that can be added to a ComputeNodeGraph
- [ComputeNodeGraph.LibraryReference](computenodegraph/libraryreference.md)
  A Metal library and an optional bundle identifier that locates shader functions.
### Node parameters and connections
- [struct PortReference](portreference.md)
  A reference to another group’s values.
- [enum BinaryOperation](binaryoperation.md)
  An enumeration of binary operations.
- [enum UnaryOperation](unaryoperation.md)
  An enumeration of single-operand operations.
- [enum StandardLibraryFunction](standardlibraryfunction.md)
### Simulation-stage nodes
- [element](element.md)
  A set of nodes for reading and writing the current element within a particle simulation.
- [emitter](emitter.md)
  A set of nodes for the emission stage that control how often and how many elements a simulation spawns.
- [initialize](initialize.md)
  A set of nodes for the initialization stage that set an element’s starting state.
- [module](module.md)
  A set of nodes that mutate per-particle state, including position, velocity, color, size, and lifetime.
- [output](output.md)
  A set of nodes for the output stage that adjust an element’s appearance without modifying its underlying state.
- [force](force.md)
  A set of nodes that apply physics forces to particles, including gravity, drag, noise, and twist.
### Utility nodes
- [graph](graph.md)
  A set of nodes that provide graph-wide information, such as time and coordinate-space transforms, usable in any stage.
- [group](group.md)
  A set of nodes for querying the group of the current particle. Available only when the simulation uses a grouped or strips element grouping.
- [texture](texture.md)
  A set of nodes for the texture stage that sample and generate texture data.
- [random](random.md)
  A set of nodes that generate pseudo-random scalars and vectors.
- [matrix4x4f](matrix4x4f.md)
  A set of nodes that transform positions and directions with single-precision 4×4 matrices.
- [matrix4x4h](matrix4x4h.md)
  A set of nodes that transform positions and directions with half-precision 4×4 matrices.
- [Viewpoint viewpoint()](viewpoint-swift.func.md)
  Returns the current viewpoint, if one is provided.
- [void element_integrate()](element_integrate.md)
- [float4 texture_sample(texture, uv)](texture_sample.md)
- [float4 texture_sample1d(texture, u)](texture_sample1d.md)
- [void orient_to_velocity()](orient_to_velocity.md)
  Orient the particle by setting its `axisY` to the velocity’s current direction.
- [void gridDebugCells(grid)](griddebugcells.md)
- [void gridFromPoints(gridStorage, inputPositions, inputFlags)](gridfrompoints.md)
- [void spawn_demo()](spawn_demo.md)
### Running a simulation
- [class ComputeGraphSimulation](computegraphsimulation.md)
  A simulation of particles, which use a single pipeline.
- [struct ElementSpawnParameters](elementspawnparameters.md)
  Parameters used to configure the initial state of a particle when it’s spawned in the simulation.
- [enum ElementGrouping](elementgrouping.md)
  An enumeration of how elements are grouped.
- [ComputeGraphSimulation.SimulationRate](computegraphsimulation/simulationrate-swift.struct.md)
  Specifies the rate and mode for simulation.
- [enum Sorting](sorting.md)
  An enumeration of sorting modes.
### Graph resources
- [ComputeNodeGraph.SamplerSettings](computenodegraph/samplersettings.md)
- [ComputeNodeGraph.SwizzleChannels](computenodegraph/swizzlechannels.md)
- [enum AddressSpace](addressspace.md)
  A GPU memory address space.
### Geometry and simulation inputs
- [ComputeNodeGraph.Topology](computenodegraph/topology.md)
  The primitive topology used to assemble output geometry for an output stage.
- [enum CoordinateSpace](coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [ComputeNodeGraph.StructureLayout](computenodegraph/structurelayout.md)
- [enum StripOrientation](striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct Viewpoint](viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.
- [struct MouseParams](mouseparams.md)
  Parameters describing mouse interaction in 3D space.
### Functions
- [void filteredLinesFromNeighbors(grid, positions, groupings, outputSegments, maxDistance)](filteredlinesfromneighbors.md)
- [void linesFromNeighbors(grid, positions, outputSegments, maxDistance)](linesfromneighbors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ComputeGraph)*