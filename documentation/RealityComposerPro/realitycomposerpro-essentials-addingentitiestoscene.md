# Adding entities and assets to a scene

**Framework**: Reality Composer Pro

Import assets to design Reality Composer Pro scenes for your app.

#### Overview

In Reality Composer Pro, you build scenes from entities and the assets you import. For background on entities, scenes, and the workspace, see [`Navigating the Reality Composer Pro workspace`](realitycomposerpro-essentials-workspaceoverview.md).

![A screenshot of a new, empty Reality Composer Pro project.](/images/RealityComposerPro/EmptyProject@2x.png)

##### Add Entity Assets to Your Project

To create an entity, in the Project Browser, click **+** and then select **Entity** from the menu. Repeat as needed. Alternatively, create non-asset entities directly in the Scene Hierarchy by Control-clicking an entity and then selecting **Add Child Entity**. If you close a scene’s tab and need to reopen it, double-click the entity file in the Project Browser. To remove a scene, delete the scene’s file in the Project Browser.

![A screenshot of the Reality Composer Pro Project Browser with the + (Add) menu open, showing the Entity option.](/images/RealityComposerPro/ProjectBrowserMenuBar@2x.png)

#### Import Assets to Your Project

In Reality Composer Pro, you design scenes by adding or importing **assets** into your project. You can import content in multiple ways, including USD and other files, into Reality Composer Pro.

##### Import Content From the Main Menu

From the Reality Composer Pro main menu, click **File** and then click **Import File**. This imports one or more files into your project, such as a PNG file to use for a texture, an audio file, or a USD file. Tip: You can also drag and drop asset files into Project Browser to import them.

![A screenshot of the Reality Composer Pro main File menu showing the Import File option.](/images/RealityComposerPro/ImportMenu@2x.png)

> ❗ **Important**: When you import a legacy project, Reality Composer Pro does not use .usd as its project file type. Reality Composer Pro saves any changes you make to the Reality Composer Pro project file, not the original .usd file.

When you import assets, you can find them in the Project Browser. Imported assets also include their dependencies.

##### Import Content From the Project Browser

From the Project Browser, Control-click the top-level project folder and then click **Import File**. Browse to the files you want to import, select them, and then click **Open**.

Alternatively, in the Project Browser, click the **Import** icon to import assets.

![A screenshot of the Reality Composer Pro Project Browser highlighting the Import icon.](/images/RealityComposerPro/ProjectBrowserImport@2x.png)

Reality Composer Pro can represent many assets as entities within a scene. However, not all assets can become entities. For example, image files don’t become entities when you add them to a scene. Reality Composer Pro only uses image assets indirectly — for example, as a source texture for materials built in Shader Graph. If you drag an image asset into the scene, nothing happens.

#### Review Import Behavior for Assets

- Reality Composer Pro treats all imported assets as read-only files; that is, Reality Composer Pro converts imported `.usd` files to entity assets in the Project Browser. Reality Composer Pro doesn’t propagate changes back to the imported `.usd` source file, although Reality Composer Pro provides options to export changes back to the original source `.usd` file.

- Reality Composer Pro projects can contain assets that aren’t used in any scenes. Xcode still compiles these assets into your app, and your app can load them at runtime. Reality Composer Pro compiles assets into `.reality` files.

#### Add Assets From the Project Browser

Drag the asset’s file from the Project Browser into the Viewport to create an instance of the entity in the scene. Alternatively, drag the asset to the Scene Hierarchy to instantiate an entity. After you add the assets, the Project Browser displays all available asset files for use in your project.

#### Compose a Scene

All RealityKit entities in a scene exist at a specific position, orientation, and scale, even if the entity has no visual representation.

When you select an entity in the viewport or Scene Hierarchy, Reality Composer Pro displays a manipulator over the selected entity in the viewport. Each of the Reality Composer Pro manipulator’s colors is tied to a different axis in 3D space. Red indicates the *x*-axis, green indicates the *y*-axis, and blue indicates the *z*-axis.

You can manipulate an entity in the following ways:

- **Moving entities** — To move the selected entity around in the viewport, drag the small colored cone that corresponds to the axis you want to move it along. Alternatively, drag the entity itself to move it freely relative to your viewing angle.
- **Rotating entities** — To rotate the selected entity, click on the manipulator’s rotation control, shown as a circle, and drag in a circular motion. The viewport’s manipulator shows one rotation control at a time. To rotate an entity on one of the other axes, click on the corresponding ring for the axis you want to rotate.
- **Scaling entities** — To scale the selected entity uniformly, drag the manipulator handles away from the entity’s origin to scale it up, or drag toward the entity’s origin to scale it down.

![A picture of the Reality Composer Pro Move interaction object shown in the Viewport.](/images/RealityComposerPro/Gizmo@2x.png)

#### Change Entities Through the Inspector

Alternatively, you can make the same changes to the selected entity by typing new values into the Transform component in the Inspector. The Transform component stores the position, rotation, and scale for an entity.

To increment a numeric field value while dragging, hold the Option key, then click and drag over the field.

#### Override Entity Properties

When you edit an instance of a prototype and change a property’s value, the system creates an **override** for that property. Overrides let you change a property for an entity used in another scene while keeping the default value from the original scene.

To revert an override back to its initial value, in the Scene Hierarchy, Control-click the entity and then select **Remove Override**.

> **Note**: Some objects — such as scopes, materials, and node graphs — exist in the Scene Hierarchy but aren’t transformable in 3D space.

#### Create or Modify Entity Hierarchies

Each scene in Reality Composer Pro contains hierarchies of all the RealityKit entities underneath the default scene’s Root. Reality Composer Pro displays these hierarchies in the Scene Hierarchy panel.

Entities can also have relationships with other entities that determine how they move relative to the other object. For example, an entity might contain multiple meshes inside a transform. You can change each mesh to override its initial location; the override persists when you manipulate the mesh’s container.

##### Change the Relationship Between Entities

To change the relationship between entities:

- In the Scene Hierarchy panel, drag the entity onto its intended parent entity.
- To make an entity the root entity in a scene, drag the selected entity to the Root transform at the top of the Scene Hierarchy.

#### Add Components to Entities

Reality Composer Pro is built on RealityKit’s Entity Component System (ECS). For background on ECS, see the [`RealityKit Developer Documentation`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/).

You can add and configure components to entities in Reality Composer Pro, including built-in RealityKit components and any custom components located in the Sources folder of your Reality Composer Pro Swift package.

To add a component to an entity:

- Select the entity in either the Scene Hierarchy or the viewport.
- At the bottom-right of the Inspector, click **Add Component** to view a list of available components for the entity. Alternatively, press the Space bar to view available components.

#### Create Custom Components From Xcode

You can create new custom components in Reality Composer Pro and then edit them in Xcode. First, integrate your project with an Xcode project.

For more information, see [`Linking an Xcode project`](realitycomposerpro-essentials-linkingxcodeproject.md).

#### Activate and Deactivate Scene Entities

As you continue to build in Reality Composer Pro, scenes can get very complex and may contain overlapping entities. To help simplify a scene, you can deactivate entities to remove them from the viewport and your scene without removing them from the current project.

![A screenshot of the Scene Hierarchy context menu in Reality Composer Pro showing the Deactivate option on a selected entity.](/images/RealityComposerPro/SceneHierarchyInstancedEntityContextMenu@2x.png)

##### Deactivate an Entity

In the Scene Hierarchy, Control-click an entity and then select **Deactivate**.

> **Note**: - Xcode doesn’t compile any deactivated entities in your scenes into your app’s bundle.
- The entity still exists in your project and appears grayed out in the Scene Hierarchy without any subentities, but Reality Composer Pro hides it in the viewport.

##### Reactivate an Entity

In the Scene Hierarchy, Control-click an entity and then select **Activate**.

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Explore the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Use Reality Composer Pro’s node-based editor to build materials, animations, audio effects, and scripts without writing code.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Edit a prototype once and propagate the change to every placement of that asset in a scene.
- [Previewing content and running simulations](realitycomposerpro-essentials-previewcontentrunsimulations.md)
  Test and iterate on your scenes directly in Reality Composer Pro, with or without a linked Xcode project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-addingentitiestoscene)*