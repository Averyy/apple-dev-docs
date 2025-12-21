# Adding assets to your Reality Composer Pro scene

**Framework**: Reality Composer Pro

Import assets to design Reality Composer Pro scenes for your app.

#### Overview

Reality Composer Pro uses scenes to store your content in `.usda` files. Each Reality Composer Pro project starts with a single empty scene called `Scene` stored in a file named `Scene.usda`. A scene can contain a collection of different entities. For example, if you have a model of an biplane, you might build a scene for it containing the 3D model, smoke coming out of its engine with a particle effect, and audio representing the various sounds a plane makes. With scenes in Reality Composer Pro, your app can load those combined assets from a single file.

![A screenshot of a Reality Composer Pro project window. The window has a single tab at the top called Scene. The window is divided horizontally into two sections. The top section has three views: a navigator view of content in the scene, a viewport in the middle showing a 3D model of a toy biplane in the center, and an inspector on the right. The bottom section has four tabs, labeled Project Browser, Shader Graph, Audio Mixer, and Statistics. Project Browser is currently selected, and it’s also divided into three sections with a hierarchy on the left, a grid of icons in the middle, and an inspector on the right showing the entity hierarchy for the asset selected in the middle.](https://docs-assets.developer.apple.com/published/0838e5075126ee9f4025dae677c6c63f/RCPro-BiplaneWindow%402x.png)

You can create as many additional scenes as you need by clicking on File > New > Scene. Reality Composer Pro adds new scenes as new tabs along the top of the active scene window, and in the Project Browser as `.usda` files.

You can use multiple scenes in your Reality Composer Pro project, each driving a different [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) in the same app, by loading the scene files stored in the project package.

If you close a scene’s tab and need to reopen it, double-click on the scene’s `.usda` file in the Project Browser editor.

To remove a scene, you can delete the scene’s `.usda` file in the Project Browser.

#### Add Assets to Your Project

In Reality Composer Pro, you design scenes by importing assets into your project.

You can add new assets in the following ways:

- Click and drag the asset’s file into the Project Browser in the editor view.
- Click on the Import button on the Project Browser’s toolbar.
- Clicking on File > Import in the menu bar and select the assets to add to your project.

After you import the assets, the Project Browser displays all of the avaliable asset files for use in your project. Reality Composer Pro treats all imported assets as read-only files. Any changes you make to assets in a scene only affect that scene’s copy of the asset and are stored in the scene’s `.usda` file, not in the original asset.

To make global changes to an asset that updates for all scenes, such as replacing an imported 3D model’s materials with dynamic Shader Graph materials, import the model as a`.usdc` file instead of as a `.usdz` file, and then separately import the supporting assets you need.

To add an asset from the Project Browser to the current scene, click and drag its file to the viewport to create an entity in the scene. Alternatively, you can click and drag the asset file to the navigator view to create an entity.

Reality Composer Pro can represent many assets as entities within a scene. However, not all assets can become entities. For example, image files don’t become entities when added to a scene. Reality Composer Pro only uses image assets indirectly, such as being a source texture for materials built in Shader Graph. If you click and drag an image asset into the scene, nothing happens.

> **Note**: Reality Composer Pro projects can contain assets that aren’t used in any scenes. These assets are still compiled into your app, can be loaded at runtime, and can take full advantage of the efficient loading process for `.realitycomposerpro` files.

##### Add Assets From the Reality Composer Pro Content Library

Reality Composer Pro includes a library of 3D, audio, and material assets that you can use in your own apps. You can access the Content Library by clicking the Add button (+) located on the right side of the project window’s toolbar.

![A screenshot of a window vertically divided into two columns. The left column contains a hierarchy of labels and folders categorized by different asset types. The right column contains a six-by-six grid of icons, each showing a different 3D model and a label below it with the model’s name.](https://docs-assets.developer.apple.com/published/b3373c3a913a7fbd780ea460aacfcd48/RCPro-ContentLibrary%402x.png)

To add an asset from the Content Libary to your project, click on the icon of the Down Arrow inside a circle in the upper-right corner of the asset icon. When the download finishes, you can double-click or drag the asset into the Project Browser to add it to your project.

The Content Library organizes its content into categories to assist with filtering for applicable content for a particular project. To filter for specific content, use the Filter field located in the upper-right corner of the Content Library window.

The Content Library may receive updates to the available content with additional or removed content. This update process is usually automatic but a download image at the top-left corner of the asset’s icon appears if an asset didn’t update. Clicking the icon downloads the updated content.

##### Compose Scenes From Assets

All RealityKit entities in a scene exist at a specific position, orientation, and scale, even if the entity has no visual representation. When you select an entity in the viewport or navigator scene, Reality Composer Pro displays:

- A manipulator over the selected entity in the viewport
- Any configurable values from the entity’s components in the inspector view on the right

You can use the manipulator to move, rotate, and scale the selected entity in either local space or world space. Reality Composer Pro defines local and world space as follows:

> ❗ **Important**: Each of the Reality Composer Pro manipulator’s colors is tied to a different axis in 3D space. Red indicates the x-axis, green indicates the y-axis, and blue indicates the z-axis.

You can manipulate an entity in the following ways:

- To move the selected entity around in the viewport, click and drag the small colored cone that corresponds to the axis you want to move it along. Alternatively, you can drag the entity itself to move it freely relative to your viewing angle.
- To rotate the selected entity, click on the manipulator’s rotation control, shown as a circle, and drag in a circular motion. The viewport’s manipulator shows one rotation control at a time. To rotate an entity on one of the other axes, click on the corresponding cone for the axis you want to rotate.
- To scale the selected entity uniformly, click the rotation circle and drag away from the entity’s origin to scale it up, or drag towards the entity’s origin to scale it down. Because the entity is scaled uniformly on all three axes, it doesn’t matter which rotation handle you selected.

When you change a property value from its default, the system creates an override for that property. Overrides are a powerful way to change a property for an entity that you use in another scene while retaining the default value from the original scene. To revert an override back to its inital value, you can select the arrow icon located to the right of the property.

Some objects — such as scopes, materials, and node graphs — exist in the navigator view but aren’t transformable in 3D space.

##### Activate and Deactivate Scene Entities

As you continue to build in Reality Composer Pro, scenes can get quite complex and may contain overlapping entities. To help simplify a scene, you can deactivate entities to remove them from the viewport and your scene without removing them from the current project.

To deactivate an entity, Control-click the entity in either the viewport or the navigator view, and select Deactivate from the contextual menu. Xcode doesn’t compile any deactivated entities in your scenes into your app’s bundle.

![A screenshot of a Scene’s navigational view in Reality Composer Pro. An entity is select and showing a contextual menu. The option Deactive is highlighted.](https://docs-assets.developer.apple.com/published/3cc4649f614d82ac1da6a5efe79ca088/RCPro-EntityDeactivate%402x.png) ![A screenshot of a Scene’s navigational view in Reality Composer Pro. An entity is select and showing a contextual menu. The option Deactive is highlighted.](https://docs-assets.developer.apple.com/published/3cc4649f614d82ac1da6a5efe79ca088/RCPro-EntityDeactivate%402x.png)

The entity still exists in your project and displays in the navigation view, now grayed out and without any subentities, but it’s hidden in the viewport.

To reactivate an entity, Control-click the entity in the navigator view and select Activate from the contextual menu.

##### Add Components to Entities

RealityKit follows a design pattern called Entity Component System (ECS). In ECS, you store data on an entity using components and then implement entity behavior by writing systems that use the data from those components. You can add and configure components to entities in Reality Composer Pro, including both built-in RealityKit components and any custom components located in the Sources folder of your Reality Composer Pro Swift package.

##### Create or Modify Entity Hierarchies

Each scene file in Reality Composer Pro contains hierarchies of all of the RealityKit entities underneath the default scene’s Root. Entities can have relationships with other entites that determine how they move relative to the other object. For example, a `.usdz` model has multiple meshes contained in a transform. You can manipulate the individual meshes to create an override from its inital location that persists when you manipulate the mesh’s container.

You can change the relationship between entities in the navigation view by clicking on an entity in the navigator view and dragging it onto the other entity you want it to be part of. For certain assets — like .usdz files — you can’t change their hierarchical relationships.

To make an entity the root entity in a scene, drag the selected entity to the Root transform at the top of the navigator view.

##### Reuse Assets with References

If your project has multiple scenes that share assets, you can utilize references to avoid creating duplicate assets. A  acts similar to an alias in Finder — it points to the original asset and functions as if it were another copy of that asset.

To create a reference to an asset or another entity in a different scene, select the entity in the viewport or navigator view and click the Add button (+) located at the bottom of the references section in the inspector panel.

![A screenshot of Reality Composer Pro’s inspector panel with the References section in focus. The References section contains a single item named ToyBiplane.usdz.](https://docs-assets.developer.apple.com/published/5d956fb010e3a500894050e58024a9ae/RCPro-References%402x.png)

You can select a version of the same entity in a different scene by clicking on the scene’s `.usda` file in the pop-up view of the Project Browser and choose the entity you want to link to from that scene’s hiearchy. When complete, the selected entity becomes a copy of the entity you linked to.

![A screenshot of Reality Composer Pro’s Project Browser Tab. There are five icons in the files view with Untiled Scene.usda selected with an outline. The inspector view shows the contents of the selected file with a reference to the cup_saucer_set asset and a reference material.](https://docs-assets.developer.apple.com/published/3e8180d3392cec986f9b8791f61bc8ab/RCPro-EntityReference%402x.png)

If you make any changes to a linked asset in one scene, the changes affects every linked reference in other scenes.

## See Also

- [Creating a Reality Composer Pro package in your app](creating-a-reality-composer-pro-package-in-your-app.md)
  Discover how to add a new or existing Reality Composer Pro project as a package to your app in Xcode.
- [Configuring the Reality Composer Pro project window](configure-the-reality-composer-pro-project-window.md)
  Change the appearance of the Reality Composer Pro project window by showing and hiding views, and learn to navigate your content.
- [Building and running Reality Composer Pro scenes in your app](build-and-run-reality-composer-pro-scenes-in-your-app.md)
  Preview scenes on your visionOS device and learn how to load them in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/adding-assets-into-your-reality-composer-pro-scene)*