# Adding entities and assets to a scene

**Framework**: Reality Composer Pro

Import assets to design Reality Composer Pro scenes for your app.

#### Overview

In Reality Composer Pro, you build scenes from entities and the assets you import. For background on entities, scenes, and the workspace, see [`Navigating the Reality Composer Pro workspace`](realitycomposerpro-essentials-workspaceoverview.md).

![A screenshot of a new, empty Reality Composer Pro project.](https://docs-assets.developer.apple.com/published/c4ba14b717f1f2b8a70e71064f9a0283/EmptyProject%402x.png)

##### Adding Entity Assets to Your Project

To create an entity, click + in the **Project Browser** and select **Entity** from the menu. Repeat as needed.

Alternatively, create non-asset entities directly in the Scene Hierarchy by Control-clicking an entity and selecting **Add Child Entity**.

If you close a scene’s tab and need to reopen it, double-click the entity file in the Project Browser editor.

To remove a scene, delete the scene’s file in the Project Browser.

![A screenshot of the Reality Composer Pro Project Browser with the + (Add) menu open, showing the Entity option.](https://docs-assets.developer.apple.com/published/a0a7fd02056482d0e39fc2a306739740/ProjectBrowserMenuBar%402x.png)

##### Importing Assets to Your Project

In Reality Composer Pro, you design scenes by adding or importing **assets** into your project. You can import content in multiple ways, including USD and other files, into Reality Composer Pro.

##### Importing Content From the Main Menu

From the Reality Composer Pro main menu, click File and then click **Import File**.

This imports one or more files into your project, such as a PNG file to use for a texture, an audio file, or a USD file.

> 💡 **Tip**: You can also drag and drop asset files into Project Browser to import them.

![A screenshot of the Reality Composer Pro main File menu showing the Import File option.](https://docs-assets.developer.apple.com/published/af654a83e49fb0ed3d038aa0f5beda72/ImportMenu%402x.png)

> ❗ **Important**: When you import a legacy project, Reality Composer Pro does not use .usd as its project file type. Reality Composer Pro saves any changes you make to the Reality Composer Pro project file, not the original .usd file.

When you import assets, you can find them in the Project Browser. Imported assets also include their dependencies.

##### Importing Content From the Project Browser

- From the Project Browser, Control-click the top-level project folder and then click **Import File**.
- Browse to the files you want to import, select them, and click **Open**.

Alternatively, in the Project Browser, click the **Import** icon to import assets.

![A screenshot of the Reality Composer Pro Project Browser highlighting the Import icon.](https://docs-assets.developer.apple.com/published/ce4ee4911fe2b177bc2f23c8095e6f32/ProjectBrowserImport%402x.png)

Reality Composer Pro can represent many assets as entities within a scene. However, not all assets can become entities. For example, image files don’t become entities when you add them to a scene. Reality Composer Pro only uses image assets indirectly — for example, as a source texture for materials built in Shader Graph. If you drag an image asset into the scene, nothing happens.

##### Important Notes for Imported Assets

- Reality Composer Pro treats all imported assets as read-only files; that is, Reality Composer Pro converts imported .usd files to entity assets in the Project Browser. Reality Composer Pro doesn’t propagate changes back to the imported .usd source file, although options exist to export changes back to the original source .usd file.
- Reality Composer Pro projects can contain assets that aren’t used in any scenes. Xcode still compiles these assets into your app, and your app can load them at runtime. Reality Composer Pro only exports Reality files.

##### Adding Assets From the Project Browser

- Drag the asset’s file from the Project Browser into the Viewport to create an instance of the entity in the scene. Alternatively, drag the asset to the Scene Hierarchy to instantiate an entity.
- From the Project Browser tool, click the **Import** icon.

After you import the assets, the Project Browser displays all available asset files for use in your project.

##### Composing Scenes

All RealityKit entities in a scene exist at a specific position, orientation, and scale, even if the entity has no visual representation.

When you select an entity in the viewport or Scene Hierarchy, Reality Composer Pro displays a manipulator over the selected entity in the viewport. Each of the Reality Composer Pro manipulator’s colors is tied to a different axis in 3D space. Red indicates the *x*-axis, green indicates the *y*-axis, and blue indicates the *z*-axis.

You can manipulate an entity in the following ways:

- **Moving entities** — To move the selected entity around in the viewport, drag the small colored cone that corresponds to the axis you want to move it along. Alternatively, drag the entity itself to move it freely relative to your viewing angle.
- **Rotating entities** — To rotate the selected entity, click on the manipulator’s rotation control, shown as a circle, and drag in a circular motion. The viewport’s manipulator shows one rotation control at a time. To rotate an entity on one of the other axes, click on the corresponding ring for the axis you want to rotate.
- **Scaling entities** — To scale the selected entity uniformly, drag the manipulator handles away from the entity’s origin to scale it up, or drag toward the entity’s origin to scale it down.

![A picture of the Reality Composer Pro Move interaction object shown in the Viewport.](https://docs-assets.developer.apple.com/published/e389046122756a15e695de79b122c223/Gizmo%402x.png)

##### Changing Entities Through the Inspector

Alternatively, you can make the same changes to the selected entity by typing new values into the Transform component in the Inspector. The Transform component stores the position, rotation, and scale for an entity.

To increment a numeric field value while dragging, hold the Option key, then click and drag over the field.

##### Property Overrides

When you edit an instance of a prototype and change a property’s value, the system creates an **override** for that property. Overrides let you change a property for an entity used in another scene while keeping the default value from the original scene.

To revert an override back to its initial value, in the Scene Hierarchy, Control-click the entity and then select **Remove Override**.

> **Note**: Some objects — such as scopes, materials, and node graphs — exist in the Scene Hierarchy but aren’t transformable in 3D space.

##### Creating or Modifying Entity Hierarchies

Each scene in Reality Composer Pro contains hierarchies of all the RealityKit entities underneath the default scene’s Root. Reality Composer Pro displays these hierarchies in the Scene Hierarchy panel.

Entities can also have relationships with other entities that determine how they move relative to the other object. For example, an entity might contain multiple meshes inside a transform. You can change each mesh to override its initial location; the override persists when you manipulate the mesh’s container.

##### Changing the Relationship Between Entities

To change the relationship between entities:

- In the Scene Hierarchy panel, drag the entity onto its intended parent entity.
- To make an entity the root entity in a scene, drag the selected entity to the Root transform at the top of the Scene Hierarchy.

##### Adding Components to Entities

Reality Composer Pro is built on RealityKit’s Entity Component System (ECS). For background on ECS, see the RealityKit documentation.

You can add and configure components to entities in Reality Composer Pro, including built-in RealityKit components and any custom components located in the Sources folder of your Reality Composer Pro Swift package.

To add a component to an entity:

- Select the entity in either the Scene Hierarchy or the viewport.
- At the bottom-right of the Inspector, click **Add Component** to view a list of available components for the entity. Alternatively, press the Space bar to view available components.

##### Creating Custom Components From Xcode

You can also create new custom components in Reality Composer Pro and then edit them in Xcode. First, integrate your project with an Xcode project.

For more information, see [`Linking an Xcode project`](realitycomposerpro-essentials-linkingxcodeproject.md).

##### Activating and Deactivating Scene Entities

As you continue to build in Reality Composer Pro, scenes can get very complex and may contain overlapping entities. To help simplify a scene, you can deactivate entities to remove them from the viewport and your scene without removing them from the current project.

![A screenshot of the Scene Hierarchy context menu in Reality Composer Pro showing the Deactivate option on a selected entity.](https://docs-assets.developer.apple.com/published/9d5cefe47681a069a8dd491546cea384/SceneHierarchyInstancedEntityContextMenu%402x.png)

##### Deactivating an Entity

In the Scene Hierarchy, Control-click an entity and then select **Deactivate**.

> **Note**: - Xcode doesn’t compile any deactivated entities in your scenes into your app’s bundle.
- The entity still exists in your project and appears grayed out in the Scene Hierarchy without any subentities, but Reality Composer Pro hides it in the viewport.

##### Reactivating an Entity

In the Scene Hierarchy, Control-click an entity and then select **Activate**.

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Navigate the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Add and connect nodes in Reality Composer Pro to create materials, animations, audio effects, scripts, and more.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Reuse a single asset across many scene placements by editing prototypes once and propagating the changes to every instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-addingentitiestoscene)*