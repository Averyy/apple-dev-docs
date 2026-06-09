# Navigating the Reality Composer Pro workspace

**Framework**: Reality Composer Pro

Navigate the panes and toolbars that make up the Reality Composer Pro editing environment.

#### Overview

This article describes how to navigate the Reality Composer Pro workspace and gives a detailed overview of its four main sections: Hierarchy, Viewport, Project Browser, and Inspector (including the Preview area).

![An annotated screenshot of an empty Reality Composer Pro project, highlighting the four main panes: Hierarchy, Viewport, Project Browser, and Inspector.](https://docs-assets.developer.apple.com/published/6358581971f04ea168a3a38d38f011ab/Overview%402x.png)

##### Browse the Scene Hierarchy

The Scene Hierarchy shows the hierarchy of all assets, components, and entities for the scene currently opened in the Viewport.

From the Hierarchy, you can add, remove, copy, paste, rename, and drag items directly in the hierarchy tree. Control-click an item to open a context menu with more options.

##### Hierarchy Top Icons

- Hide/Show Hierarchy pane (toggle)

##### Hierarchy Item Select Icons

- Lock/unlock asset — Locks the asset and prevents changes.
- Show/hide asset — Toggle to show or hide the asset in the viewport.

> **Note**: Locking, unlocking, hiding, and unhiding assets don’t affect exported files — these editor-only actions help you organize and focus on specific entities. To deactivate an entity, Control-click it and choose Deactivate.

##### Hierarchy Bottom Icons

- **Add to Hierarchy** — Add an empty or geometry entity to your hierarchy within the currently selected part of the hierarchy. When an entity is selected, you can also add components and imported assets from your Project Browser.
- **Show Components —** Toggle components on/off so you can view Entities only.
- **Filter (Command-F)** — Type to search/filter the hierarchy view. For example, typing “robot” limits the hierarchy view to display all items in the hierarchy with robot in the name. You can also use the filter to find components.

![Control-clicking a Transformation object compared to Control-clicking a 3D object in the Reality Composer Pro Hierarchy.](https://docs-assets.developer.apple.com/published/9d5cefe47681a069a8dd491546cea384/SceneHierarchyInstancedEntityContextMenu%402x.png)

In the Hierarchy, you can also **Control-click** an entity to see all available options for that entity. For example, compare available options in the examples below.

##### Manage Project Files in the Project Browser

The project browser keeps track of all the assets or files in the project. This is your main window for browsing, opening, and managing all of the files and folders in your project. From the browser, you can perform all standard file operations (copy, paste, delete, and so on) on the files and folders in your project. You can also create or import assets — such as USD files, images, and audio files — into your project.

Clicking a file in the project browser also shows more information in the Inspector, where you can view properties and any components associated with the file, as well as a thumbnail in the Preview tab for certain types of files.

##### Project Browser Menu Bar Left to Right

- Close Project Browser
- Console — Open to view console output.
- Open/close browser side panel
- New Folder
- New Asset
- Import Asset
- Back / Forward
- Show as list
- Show as grid
- Thumbnail size (slider)
- Search project

> **Note**: When you open an asset in the project browser, it opens in a new tab at the top of the Viewport.

##### Manipulate Content in the Viewport

The Viewport displays your project’s assets and scenes. Use the viewport modes to change how you interact with content and navigate the scene.

##### Launch Bar

![A screenshot of the Launch bar at the top of the Reality Composer Pro Viewport.](https://docs-assets.developer.apple.com/published/27934496e598a666040f0a169decc78b/launchbar%402x.png)

Use the viewport simulator toolbar to:

- **Play (button)** — Runs the simulation in the viewport of the currently viewed asset.
- **Simulate** — Plays the scene in the viewport.
- **Preview on Device** — View the simulation on a virtual device. This feature extends Reality Composer Pro to Apple Vision Pro. The companion app shows your editor changes as real-time previews, so you can compose the scene directly on device.
- **Run with Xcode** — Run the simulation using an attached Xcode project. This allows you to preview content on a device, but in the context of your app.

![A screenshot of additional entities opened from the Hierarchy view appearing as tabs in the Reality Composer Pro Viewport.](https://docs-assets.developer.apple.com/published/e4af8b33b0576cc0939d58b03dc61165/WorkspaceTab%402x.png)

> 💡 **Tip**: If you’ve opened additional entities from the Hierarchy view, they appear as tabs.

##### Viewport Icons

![A screenshot of the Reality Composer Pro Viewport icons for selecting, moving, rotating, scaling, snapping, transforming, and pivoting.](https://docs-assets.developer.apple.com/published/4f108c6f935ca889b333766377ed59ae/GizmoControl%402x.png)

- **Select** — Click to select an object in the Viewport. In the Viewport, you can also: - **Click-and-drag** to select an object or group of objects (Marquee select)
- **Shift-click** to select multiple individual items

After selecting one or more items, you can then click Move, Rotate, or Scale to interact with the selected objects.

- **Move** — Move the selected object in the viewport on the X, Y, or Z-axis.
- **Rotate** — Rotate the selected object in the viewport on the X, Y, or Z-axis.
- **Scale** — Scale the selected object up or down in the viewport on the X, Y, or Z-axis.
- **Enable Snapping** — Snap interactions (move, rotate, scale) to the grid.
- **Snap Distance** — If snapping is enabled, this value defines the distance for snapping the object to the grid.
- **Transform Space** —The space affected by your changes: - **World** — Manipulate and set values relative to the scene.
- **Local** — Manipulate and set transform values relative to the parent object.
- **Pivot Point** — Defines the focal object for the Move, Rotate, or Scale interaction. First Selected, Last Selected, Center, or Bounding Box.

##### Move Rotate and Scale Entities

![A screenshot of the manipulator gizmo on a selected entity in the Reality Composer Pro Viewport, with colored axes for moving, rotating, and scaling.](https://docs-assets.developer.apple.com/published/e389046122756a15e695de79b122c223/Gizmo%402x.png)

Click a mode (Move, Rotate, or Scale) in the bottom-left of the viewport and then use the **manipulator** to manipulate the asset.

The Q, W, E, and R keys on the keyboard are also mapped to the Select, Move, Scale, and Rotate functions.

Each color in the manipulator corresponds to a specific axis:

- **Red** — Move, Rotate, or Scale on the **X-axis only**
- **Green** — Move, Rotate, or Scale on the **Y-axis only**
- **Blue** — Move, Rotate, or Scale on the **Z-axis only**
- **Gray (center)** — Free Move, Rotate, or Scale on any axis

> 💡 **Tip**: For the Scale and Move tools, you can also click and drag the squares, which affects the entity in the constraint of the plane.

Use the scroll wheel to zoom in/out of the Viewport.

##### Viewport Toolbar Visualization Icons

![A screenshot of the Viewport toolbar visualization icons in Reality Composer Pro, including camera, lighting, debug visualization filter, and rendering mode controls.](https://docs-assets.developer.apple.com/published/94ab59502bc6db8ffb4ad7242cc054c7/VisualizationToolbar%402x.png)

- **Select Camera** — Select a camera in the scene for the viewport to use. By default, the Viewport shows only **Default Camera** unless you’ve added a Camera component to the current entity. Select Default Camera to reset the view.
- **Lighting Environment Settings —** Change the Environment Lighting Asset used to light the scene.
- **Filter Component Debug Visualization** — Toggles on/off one or more component plugins so you can see how they affect everything in the Viewport. Includes: - [`CharacterControllerComponent`](https://developer.apple.com/documentation/RealityKit/CharacterControllerComponent)
- [`CollisionComponent`](https://developer.apple.com/documentation/RealityKit/CollisionComponent)
- Decal
- Diffuse Light Probe Group
- Diffuse Light Probe Marker
- [`DirectionalLightComponent`](https://developer.apple.com/documentation/RealityKit/DirectionalLightComponent)
- [`DockingRegionComponent`](https://developer.apple.com/documentation/RealityKit/DockingRegionComponent)
- [`ModelComponent`](https://developer.apple.com/documentation/RealityKit/ModelComponent)
- Navigation Mesh
- [`PointLightComponent`](https://developer.apple.com/documentation/RealityKit/PointLightComponent)
- [`IKComponent`](https://developer.apple.com/documentation/RealityKit/IKComponent)
- [`SpotLightComponent`](https://developer.apple.com/documentation/RealityKit/SpotLightComponent)
- [`VirtualEnvironmentProbeComponent`](https://developer.apple.com/documentation/RealityKit/VirtualEnvironmentProbeComponent)
- **Rendering Visualization Modes** — Change the rendering visualization mode to see how different modes affect the asset. Options include: - Normals
- Tangent
- Bitangent
- Base Color
- Texture Coordinates
- Final Color
- Final Alpha
- Roughness
- Metallic
- Ambient Occlusion
- Specular
- Emissive
- Clearcoat
- Clearcoat Roughness
- Lighting Diffuse
- Lighting Specular

##### Inspect Entity Properties

The inspector panel is where you can:

- View, add, or change **components** such as transforms, materials, and animations that are applied to the currently selected entity; or
- View, add, or change **inputs** and **outputs** for a currently selected Node, Nodes, or Subgraph in the Graph editor.
- Edit asset metadata, such as the import options for a USD file.

When an entity is selected, click **Add Component** to add more components.

##### Inspector View Icons Top Right

![A screenshot of the Inspector view icons at the top right of the Reality Composer Pro Inspector pane, including Lighting Tools and the Hide/Show Inspector toggle.](https://docs-assets.developer.apple.com/published/ec25bb1eeccb387fd880dada35374148/InspectorButton%402x.png)

- **Lighting Tools** — Use to select the Lightmap Bake Quality (Low, Medium, High, Production), and then select **Bake Lightmap** or **Capture Environment**.

> 💡 **Tip**: You can open a Lightmap Preview (**Tab** > **Lightmap Preview**) to view bake results.

- **Hide/Show Inspector** (toggle) — Open/close the Inspector pane.

Together, the Hierarchy, Project Browser, Viewport, and Inspector form the core editing workflow in Reality Composer Pro: locate assets in the Project Browser, organize them in the Hierarchy, edit them in the Viewport, and refine their components in the Inspector.

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Add and connect nodes in Reality Composer Pro to create materials, animations, audio effects, scripts, and more.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Reuse a single asset across many scene placements by editing prototypes once and propagating the changes to every instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-workspaceoverview)*