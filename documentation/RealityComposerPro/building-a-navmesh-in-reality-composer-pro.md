# Building a navmesh in Reality Composer Pro

**Framework**: Reality Composer Pro

Configure a navigation mesh in Reality Composer Pro to define walkable areas and paths for AI-controlled entities in your scene.

#### Overview

A Reality Composer Pro navmesh provides a representation of a scene’s navigable surfaces, simplifying pathfinding for AI-driven NPCs (non-player characters) in complex 3D environments.

#### Create a Navigation Named Layers File

To create and use navigation layers, areas, and flags, create a Navigation Named Layers file to store the mappings of the indexes to names. In your Navigation Mesh and Navigation components, you can reference these entries by name. When you export to a reality file, the indexes match the structs in Swift code, enabling you to reference them in code.

1. In the **Project Browser**, Control-click to create a new file, then select **Navigation Named Layers**.
2. Expand the drop-downs for **Layers**, **Areas**, and **Flags** to add or remove entries and rename them.

#### Create a Navmesh

In the Scene Hierarchy, Control-click a scene entity (World, for example), then click **Add Component** > **Navigation Mesh**. In the Inspector, under **Navigation Mesh Component**, click **[+]** to add a new Navigation Mesh. Add a Navigation Named Layers file to your Navigation Mesh Component. The Navigation Mesh Component dropdowns for Layers, Areas, and Flags will be populated with the entries from the Named Layers File. Add a Layer to identify your mesh. Entities in the scene reference this layer to access the map of available paths. For more information about adding a layer, see doc:NavigationMeshLayers.

> **Note**: If you leave Navigation Mesh Layer blank, entities default to the first mesh used in the scene.

Configure the properties for each of the following sections, described later in this article:

- Shapes
- Off Mesh Connections
- Generation Parameters
- Tags

Click **Generate Navigation Mesh** when you’re ready.

![A screenshot of a basic Navigation Mesh in a Reality Composer Pro project.](https://docs-assets.developer.apple.com/published/c9d804804fb267b440600dd105de9f33/NavMesh1%402x.png)

> 💡 **Tip**: You can generate a navmesh without opening each component individually. Above the Inspector, click **Lighting Tools** (the shaded circle icon). In Baking options, open the **Selected Navigation Mesh** drop-down menu and choose a navigation mesh to generate — or select **All** to generate all navigation meshes for the scene — then click **Generate Navigation Mesh**.

#### Define Navigation Mesh Shapes

The shape setting controls the area of the scene the generated mesh covers. By default, the shape encompasses the entire scene. To generate the mesh for only part of the scene, drag the bounding box to the desired area.

Shape selection only includes entities at or below the current hierarchy level. For example, in the following hierarchy:

```None
World
- Entity 1
- Entity 2
  - Entity 3
```

- If you place the navigation mesh component on Entity 2, it selects only Entity 2 and Entity 3.
- If you place it on World, it selects everything.

#### Add Off Mesh Connections

Off-mesh connections let you link points on the mesh that normal geometry does not connect. For example, use an off-mesh connection to create a connection between two points that only certain entities can traverse outside the standard mesh connections.

Click **[+]** to add an off-mesh connection, then use the Move tool to position the connection.

- You can create as many off-mesh connections as you want.
- You can give off-mesh connections unique names, which other components and graphs can reference — such as triggering a specific animation when an entity moves along the off-mesh connection.

#### Control Navigation Mesh Generation with Parameters

These parameters give you more granular control over how Reality Composer Pro generates the navigation mesh. For example, to support larger characters increase **Character Radius**; to prevent the mesh from covering steep terrain, reduce **Walkable Slope Angle**.

**Basic**

- **Cell Size**: The cell size (in world units) to use when sampling the source geometry.
- **Cell Height**: The cell height (in world units) to use when sampling the source geometry.
- **Character Height**: The minimum floor-to-ceiling height for the floor to be considered walkable.
- **Walkable Climb Height**: Maximum ledge height that is considered walkable.
- **Walkable Slope Angle**: Maximum slope that is considered walkable.
- **Character Radius**: Distance to erode or shrink the walkable area of the height field away from obstructions. Use this to prevent larger characters from traversing parts of the mesh.

**Advanced**

- **Max Edge Length**: Max length for contour edges on the border of a mesh.
- **Max Simplification Error**: The maximum distance that a simplified contour’s border edges can deviate from the original raw contour.
- **Min Cells per Region**: Minimum number of cells allowed to make isolated island areas.
- **Min Cells to Merge Regions**: Regions with a span count smaller than this value merge with larger regions when possible.
- **Detail Sample Distance**: Sampling distance to use when sampling the detail mesh.
- **Detail Sample Max Error**: The maximum distance the detail mesh surface can deviate from heightfield data.
- **Max Vertices per Polygon**: Max vertices per polygon in the final created navigation mesh.
- **Partition Method**: The algorithm used to partition the height field into regions. Options: Watershed, Monotone, or Layer. - **Watershed** (default) — Produces the best meshes.
- **Monotone** — Produces the fastest meshes.
- **Layer** — Fast and handles open regions better than Monotone.

#### Use Navigation Mesh Tags to Define How Entities Move

You can use tags to control how entities traverse parts of the mesh — for example, you can use tags to prevent certain entities from traversing areas with specific tags. There are two main types of tags:

- Area — A tag that assigns an area type to a region, which entities can use when computing navigation paths. Areas can be used to assign a cost to an area.
- Flag — A binary tag that entities can use to selectively include or exclude areas when navigating.

Use a **Navigation Component **to to assign the costs for an entity to path through an area and which flags to include or ignore.

#### Add a Navigation Mesh Tag

Click **[+]** to add one or more tags to areas of the Navigation Mesh, then use the Move tool to position the selection area over the area you want to tag. For more information about adding Area and Flag tags, see doc:NavigationMeshLayers.

Use the **Position**, **Height**, and **Radius** settings to change the position and size of the tagged area.

You can have as many tags as you want in a region.

## See Also

- [Creating animation sequences](creating-animation-sequences.md)
  Build animation sequences that drive entity behavior across multiple tracks in Reality Composer Pro.
- [Creating animation sequences for auto-play](creating-animation-sequences-for-autoplay.md)
  Root an animation Sequence at the right entity, then wire it to an Animation Library Component so it plays automatically at runtime.
- [Building multi-track animation sequences](building-multi-track-animation-sequences.md)
  Root a Sequence correctly so it shows up as a clip and plays automatically at runtime.
- [Working with the Animation Graph](working-with-the-animation-graph.md)
  Build character animation state machines visually using the Animation Graph in Reality Composer Pro.
- [Building an advanced Animation Graph](building-an-advanced-animation-graph.md)
  Drive a character’s locomotion state machine from a Script Graph at runtime.
- [Defining a behavior with Behavior Trees](defining-a-behavior-with-behavior-trees.md)
  Set up and connect Behavior Tree nodes to drive entity decision-making in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/building-a-navmesh-in-reality-composer-pro)*