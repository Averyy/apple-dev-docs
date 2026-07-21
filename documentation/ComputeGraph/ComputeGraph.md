# Compute Graph

**Framework**: Compute Graph  
**Kind**: module

Build and run custom particle effects and compute simulations for RealityKit using a programmable node graph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 3.0+ (Beta)

#### Overview

Compute Graph is a node-based framework for constructing particle simulations and general-purpose GPU compute graphs in [`RealityKit`](https://developer.apple.com/documentation/RealityKit). Whereas [`ShaderGraph`](https://developer.apple.com/documentation/ShaderGraph) lets developers build material appearance through a node-based visual editor, Compute Graph provides the same graph-driven, connection-based authoring for simulation behavior. The technology targets tool and editor developers who need fine-grained, per-stage control over how particles and compute work proceeds.

The Swift API centers on a three-step compilation pipeline. Describe a simulation as a `GraphDefinition`, a directed graph of typed nodes and edges. Then assemble the graph into a `ComputeGraphAssembly`, which resolves the buffer, uniform, and texture layout the simulation requires. Compile that assembly into `ComputeGraphPipelines` to produce GPU shader code; a single set of pipelines can back multiple [`ComputeGraphSimulation`](computegraphsimulation.md) instances running concurrently. `Library` and `SyntheticNodeLibrary` let you supply custom Metal Shading Language functions as node definitions alongside the framework’s built-in set in `ComputeGraphBuiltIns`.

At runtime, [`ComputeGraphSimulation`](computegraphsimulation.md) drives GPU execution. Call [`advance(_:)`](computegraphsimulation/advance(_:).md) each frame, passing an [`ComputeGraphSimulation.AdvanceParams`](computegraphsimulation/advanceparams.md) that carries the time delta, a Metal command buffer, a compute encoder, and optional world-space transforms. Bind `GraphBuffer`, `GraphTexture`, and `GraphUniform` resources before the first advance. To inject elements programmatically, call [`spawn(elements:in:using:)`](computegraphsimulation/spawn(elements:in:using:).md) with [`ElementSpawnParameters`](elementspawnparameters.md) values that set each element’s initial position, velocity, size, color, and lifetime.

## Topics

### Simulation objects
- [class ComputeGraphSimulation](computegraphsimulation.md)
  A simulation of particles, which use a single pipeline.
### Built-in nodes
- [element](element.md)
  A set of nodes for reading and writing the current element within a particle simulation.
- [emitter](emitter.md)
  A set of nodes usable in the emission stage of a simulation, which control how often and how many elements to spawn.
- [force](force.md)
  Apply physics forces including gravity, drag, noise, and twist.
- [initialize](initialize.md)
  Nodes usable within the initialization stage of an element.
- [output](output.md)
  Nodes usable within the output stage of an element. You can use these nodes to change the appearance of an element without making modifications to the element itself.
- [module](module.md)
  Mutate per-particle state with operations such as setPosition, addPosition, setVelocity, setColor, setSize, and setLifetime.
- [graph](graph.md)
  A set of nodes usable in any stage within a ComputeGraph.
- [group](group.md)
  Nodes for querying the group for a current particle. Requires a system whose simulation stage is configured as either `strips` or `grouped`.
- [texture](texture.md)
  Nodes usable within the texture stage, for generating textures.
- [random](random.md)
  Nodes for generating pseudo-random numbers.
- [matrix4x4f](matrix4x4f.md)
  Transform positions and directions using matrix4x4f.
- [matrix4x4h](matrix4x4h.md)
  Transform positions and directions using matrix4x4h.
### Node parameters and connections
- [struct PortReference](portreference.md)
  A reference to another group’s values.
- [enum BinaryOperation](binaryoperation.md)
  An enumeration of binary operations.
- [enum UnaryOperation](unaryoperation.md)
  An enumeration of single-operand operations.
- [enum StandardLibraryFunction](standardlibraryfunction.md)
### Elements and particles
- [enum ElementGrouping](elementgrouping.md)
  An enumeration of how elements are grouped.
- [struct ElementSpawnParameters](elementspawnparameters.md)
  Parameters used to configure the initial state of a particle when it’s spawned in the simulation.
- [enum Sorting](sorting.md)
  An enumeration of sorting modes.
### Graph resources
- [enum AddressSpace](addressspace.md)
  A GPU memory address space.
### Geometry and simulation inputs
- [enum CoordinateSpace](coordinatespace.md)
  Simulation coordinate space, controlling how positions and orientations are stored.
- [enum StripOrientation](striporientation.md)
  An enumeration that specifies how a strip should be oriented.
- [struct Viewpoint](viewpoint-swift.struct.md)
  Camera viewpoint parameters in 3D space.
- [struct MouseParams](mouseparams.md)
  Parameters describing mouse interaction in 3D space.
### Structures
- [struct ComputeNodeGraph](computenodegraph.md)
### Functions
- [void element_integrate()](element_integrate.md)
- [void filteredLinesFromNeighbors(grid, positions, groupings, outputSegments, maxDistance)](filteredlinesfromneighbors.md)
- [void gridDebugCells(grid)](griddebugcells.md)
- [void gridFromPoints(gridStorage, inputPositions, inputFlags)](gridfrompoints.md)
- [void linesFromNeighbors(grid, positions, outputSegments, maxDistance)](linesfromneighbors.md)
- [void orient_to_velocity()](orient_to_velocity.md)
  Orient the particle by setting its `axisY` to the velocity’s current direction.
- [void spawn_demo()](spawn_demo.md)
- [float4 texture_sample(texture, uv)](texture_sample.md)
- [float4 texture_sample1d(texture, u)](texture_sample1d.md)
- [Viewpoint viewpoint()](viewpoint-swift.func.md)
  Returns the current viewpoint, if one is provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ComputeGraph)*