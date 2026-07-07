# Navigating the Reality Composer Pro workspace

**Framework**: Reality Composer Pro

Explore the panes and toolbars that make up the Reality Composer Pro editing environment.

#### Overview

The Reality Composer Pro workspace is organized into four main sections: Hierarchy, Viewport, Project Browser, and Inspector (including the Preview area).

Together, the Hierarchy, Project Browser, Viewport, and Inspector form the core editing workflow in Reality Composer Pro: locate assets in the Project Browser, organize them in the Hierarchy, edit them in the Viewport, and refine their components in the Inspector.

![An annotated screenshot of an empty Reality Composer Pro project, highlighting the four main panes: Hierarchy, Viewport, Project Browser, and Inspector.](https://docs-assets.developer.apple.com/published/6358581971f04ea168a3a38d38f011ab/Overview%402x.png)

#### Browse the Scene Hierarchy

The Scene Hierarchy shows the hierarchy of all assets, components, and entities for the scene currently opened in the Viewport.

From the Hierarchy, you can add, remove, copy, paste, rename, and drag items directly in the hierarchy tree. Control-click an item to open a context menu with more options.

#### Show or Hide the Hierarchy

Click the Hide/Show icon at the top of the Hierarchy to open or close it.

#### Lock or Hide Assets in the Hierarchy

These icons are available when you click on an item in the Hierarchy.

- **Lock or unlock asset** — Locks the asset and prevents changes.
- **Show or hide asset** — Toggle to show or hide the asset in the Viewport.

> **Note**: Locking, unlocking, hiding, and unhiding assets don’t affect exported files — these editor-only actions help you organize and focus on specific entities. To deactivate an entity, Control-click it and choose Deactivate.

#### Add Show or Filter Items Shown in the Hierarchy

Use the icons at the bottom of the Hierarchy to:

- **Add to Hierarchy** — Add an empty or geometry entity to your hierarchy within the currently selected part of the hierarchy. When an entity is selected, you can also add components and imported assets from your Project Browser.
- **Show Components —** Toggle components on or off to view Entities only.
- **Filter (Command-F)** — Type to search or filter the hierarchy view. For example, typing “robot” limits the hierarchy view to display all items in the hierarchy with robot in the name. You can also use the filter to find components.

![Control-clicking a Transformation object compared to Control-clicking a 3D object in the Reality Composer Pro Hierarchy.](https://docs-assets.developer.apple.com/published/9d5cefe47681a069a8dd491546cea384/SceneHierarchyInstancedEntityContextMenu%402x.png)

> 💡 **Tip**: You can also **Control-click** an entity in the Hierarchy to see all available options for that entity.

#### Manage Project Files in the Project Browser

Use the Project Browser menu bar icons to view and manage files, folders, assets, and other project files.

> 💡 **Tip**: When you open an asset in the Project Browser, it opens in a new tab at the top of the Viewport.

#### Use the Project Browser Toolbar Icons

Use the following icons to navigate and manage your project assets:

- **Close Project Browser** — Closes the Project Browser panel to give more space to the Viewport.
- **Console** — Opens the console to view output logs and build messages.
- **Open or close browser side panel** — Toggles the side panel within the Project Browser to show or hide additional file details.
- **New Folder** — Creates a new folder in the current project location.
- **New Asset** — Creates a new asset (such as a USD scene or material) in the current project location.
- **Import Asset** — Imports external files (such as USD, textures, or audio) into the project.
- **Back / Forward** — Navigates backward or forward through recently viewed locations in the Project Browser.
- **Show as list** — Displays project contents as a list view.
- **Show as grid** — Displays project contents as a grid of thumbnails.
- **Thumbnail size (slider)** — Adjusts the size of thumbnails when using the grid view.
- **Search project** — Filters the Project Browser to show only items matching your search term.

#### Interact with Content in the Viewport

The Viewport displays your project’s assets and scenes. Use the Viewport modes to change how you interact with content and navigate the scene.

#### Run Simulations From the Viewport Toolbar

Use the Viewport toolbar to preview and run simulations in the Viewport, on a simulated device, or through a connected device. For more information about previewing content, see [`Previewing content and running simulations`](realitycomposerpro-essentials-previewcontentrunsimulations.md).

![A screenshot of additional entities opened from the Hierarchy view appearing as tabs in the Reality Composer Pro Viewport.](https://docs-assets.developer.apple.com/published/e4af8b33b0576cc0939d58b03dc61165/WorkspaceTab%402x.png)

#### Manipulate Entities in the Viewport

![A screenshot of the Reality Composer Pro Viewport icons for selecting, moving, rotating, scaling, snapping, transforming, and pivoting.](https://docs-assets.developer.apple.com/published/4f108c6f935ca889b333766377ed59ae/GizmoControl%402x.png)

Click an object or entity in the Viewport to select it. You can also drag to select one or more objects (Marquee select) or Shift-click to select multiple, individual items. Use the scroll wheel to zoom in or out of the Viewport. Option-click to rotate (orbit) the view in the Viewport.

#### Move Rotate and Scale Entities

Select an entity in the Viewport, click a mode (Move, Rotate, or Scale) in the bottom-left of the Viewport, and then use the **manipulator** to manipulate the asset.

![A screenshot of the manipulator gizmo on a selected entity in the Reality Composer Pro Viewport, with colored axes for moving, rotating, and scaling.](https://docs-assets.developer.apple.com/published/e389046122756a15e695de79b122c223/Gizmo%402x.png)

The Q, W, E, and R keys on the keyboard are also mapped to the Select, Move, Scale, and Rotate functions. Each color in the manipulator corresponds to a specific axis:

- **Red** — Move, Rotate, or Scale on the **X-axis only**
- **Green** — Move, Rotate, or Scale on the **Y-axis only**
- **Blue** — Move, Rotate, or Scale on the **Z-axis only**
- **Gray (center)** — Free Move, Rotate, or Scale on any axis

> 💡 **Tip**: For the Scale and Move tools, you can also click and drag the squares, which affects the entity in the constraint of the plane.

#### Change Viewport Visualization Options

The following icons (to the right of the Select, Move, Rotate, and Scale icons) in the Viewport also let you change your visualization options in the Viewport.

- **Enable Snapping** — Snap interactions (move, rotate, scale) to the grid.
- **Snap Distance** — If snapping is enabled, this value defines the distance for snapping the object to the grid.
- **Transform Space** —The space affected by your changes: - **World** — Manipulate and set values relative to the scene.
- **Local** — Manipulate and set transform values relative to the parent object.
- **Pivot Point** — Defines the focal object for the Move, Rotate, or Scale interaction. First Selected, Last Selected, Center, or Bounding Box.

#### Preview Scenes with Different Cameras and Lighting

Preview your scene with different cameras, lighting, and visualization options by selecting the icons in the upper-right corner of the Viewport.

![A screenshot of the Viewport toolbar visualization icons in Reality Composer Pro, including camera, lighting, debug visualization filter, and rendering mode controls.](https://docs-assets.developer.apple.com/published/94ab59502bc6db8ffb4ad7242cc054c7/VisualizationToolbar%402x.png)

- **Select Camera** — Select a camera in the scene for the Viewport to use. By default, the Viewport shows only **Default Camera** unless you’ve added a Camera component to the current entity. Select Default Camera to reset the view.
- **Lighting Environment Settings —** Change the Environment Lighting Asset used to light the scene.
- **Filter Component Debug Visualization** — Overlays visual indicators in the Viewport that show how specific components affect your scene. Toggle individual components on or off to isolate their effects — for example: - [`CollisionComponent`](https://developer.apple.com/documentation/RealityKit/CollisionComponent) — Displays collision shape geometry on entities.
- [`PointLightComponent`](https://developer.apple.com/documentation/RealityKit/PointLightComponent) — Visualizes each light’s attenuation radius as a sphere.
- [`IKComponent`](https://developer.apple.com/documentation/RealityKit/IKComponent) — Displays skeletal bones and joint hierarchies overlaid on characters. All supported components — including [`CharacterControllerComponent`](https://developer.apple.com/documentation/RealityKit/CharacterControllerComponent), [`DirectionalLightComponent`](https://developer.apple.com/documentation/RealityKit/DirectionalLightComponent), [`DockingRegionComponent`](https://developer.apple.com/documentation/RealityKit/DockingRegionComponent), [`ModelComponent`](https://developer.apple.com/documentation/RealityKit/ModelComponent), [`SpotLightComponent`](https://developer.apple.com/documentation/RealityKit/SpotLightComponent), and [`VirtualEnvironmentProbeComponent`](https://developer.apple.com/documentation/RealityKit/VirtualEnvironmentProbeComponent) — appear in the dropdown.
- **Rendering Visualization Modes** — Isolate and inspect specific rendering data for the selected asset. Use geometry channel modes to check surface topology, material channel modes to verify texture assignments, and lighting modes to diagnose shading. Options include: - **Geometry Channels**: - **Normals** — Displays surface normal directions as RGB colors; useful for diagnosing shading artifacts.
- **Tangent** — Shows tangent vectors used for normal mapping.
- **Bitangent** — Shows bitangent vectors that complete the tangent space.
- **Texture Coordinates** — Visualizes UV coordinate layout as a color gradient.
- **Material channels:**
- **Base Color** — Shows the albedo (diffuse color) texture without lighting applied.
- **Roughness** — Displays the roughness map; white indicates fully rough, black indicates fully smooth.
- **Metallic** — Shows the metallic map; white indicates fully metallic surfaces.
- **Ambient Occlusion** — Displays baked ambient occlusion data.
- **Specular** — Shows specular intensity values.
- **Emissive** — Displays emissive (self-illuminating) color values.
- **Clearcoat** — Shows the clearcoat layer intensity.
- **Clearcoat Roughness** — Displays the roughness of the clearcoat layer.
- ********Output channels**: - **Final Color** — Shows the fully composited, lit output color.
- **Final Alpha** — Displays the final transparency (alpha) values.
- **Lighting Diffuse** — Shows only the diffuse lighting contribution.
- **Lighting Specular** — Shows only the specular lighting contribution.

#### View and Change Entity Properties in the Inspector

Use the Inspector panel to:

- View, add, or change **components** such as transforms, materials, and animations that are applied to the currently selected entity; or
- View, add, or change **inputs** and **outputs** for a currently selected Node, Nodes, or Subgraph in the Graph editor.
- Edit asset metadata, such as the import options for a USD file.

When an entity is selected, click **Add Component** to add more components. Use the Hide/Show Inspector icon to close or open the Inspector.

#### Bake Lightmaps with Lighting Tools

Lightmap baking is a precomputation step that renders static lighting into textures for more efficient runtime rendering. Use the Lighting tools icon in the Inspector to select the Lightmap Bake Quality (Low, Medium, High, Production), and then select **Bake Lightmap** or **Capture Environment** to run the bake.

> 💡 **Tip**: You can open a Lightmap Preview (**Tab** > **Lightmap Preview**) to view bake results.

![A screenshot of the Inspector view icons at the top right of the Reality Composer Pro Inspector pane, including Lighting Tools and the Hide/Show Inspector toggle.](https://docs-assets.developer.apple.com/published/ec25bb1eeccb387fd880dada35374148/InspectorButton%402x.png)

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Use Reality Composer Pro’s node-based editor to build materials, animations, audio effects, and scripts without writing code.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Edit a prototype once and propagate the change to every placement of that asset in a scene.
- [Previewing content and running simulations](realitycomposerpro-essentials-previewcontentrunsimulations.md)
  Test and iterate on your scenes directly in Reality Composer Pro, with or without a linked Xcode project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-workspaceoverview)*