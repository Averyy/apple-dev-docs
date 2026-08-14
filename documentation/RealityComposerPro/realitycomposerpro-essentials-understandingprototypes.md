# Reusing assets with prototypes and instances

**Framework**: Reality Composer Pro

Edit a prototype once and propagate the change to every placement of that asset in a scene.

#### Overview

In Reality Composer Pro, a **prototype** is a source asset, and an **instance** is a placement of that prototype in a scene. Dragging the asset into your scene creates a single instance of that prototype. You can place as many instances of the prototype in your scene as you want.

- If you change a prototype, Reality Composer Pro propagates those changes to every instance of that prototype in your project.
- If you make changes in the Scene Hierarchy to an instance of a prototype, Reality Composer Pro treats the changes as an **override** on the instance. Overrides don’t affect the prototype itself. Overrides appear in the Scene Hierarchy as a small dot next to the icon.

![A screenshot of the Reality Composer Pro Scene Hierarchy with a white override-indicator dot next to an instance.](/images/RealityComposerPro/SceneHierarchyCropped@2x.png)

> ❗ **Important**: When you directly assign a prototype to a component — for example, assigning a material to a model component — Reality Composer Pro may not automatically create an instance. Any edits to the material directly edit the prototype instead. To assign an instance, Control-click the material in the Project Browser, select **Instance**, and then assign the instanced material to the model component.

#### Create an Instance of a Prototype

An instance is a virtual copy of a prototype asset that you can change without affecting the source prototype.

In the Project Browser, Control-click a prototype asset, and then click **Instantiate **to create an instance of the asset.

#### Add an Instance of a Prototype to a Scene

Drag the instance from the Project Browser into the Viewport as you would any asset. Alternatively, Control-click anywhere in the Hierarchy, choose **Add Child Entity** > **From Asset**, and select the entity instance from the menu.

#### Propagate Reset or Make an Instance Unique

Once you create an instance of a prototype and make changes, you have three options when an instance and its prototype have diverged: Propagate, Reset, or Make Unique.

- Use **Propagate** when an instance has the look or behavior you want and you want every other instance of the same prototype to match. Propagating from one instance updates the source prototype, which in turn updates every other instance of the prototype in your project.
- Use **Reset** when you’ve experimented with overrides on an instance and want to discard those local edits but keep the link to the prototype. This reverts the instance’s values to the prototype’s but preserves the link so future changes to the prototype still flow through.
- Use **Make Unique** when an instance has diverged enough that tracking the prototype is no longer useful. This removes the link to the prototype and converts the instance into a standalone copy. The new copy retains the instance’s current values but no longer receives changes propagated from the original prototype.

#### Manage Prototype Overrides

Use the Inspector or the Scene Hierarchy to propagate or reset overrides on an instance. Make Unique is available only from the Scene Hierarchy.

**From the Inspector:** Control-click the entry you want to change, and then select **Propagate** or **Reset**.

![The Reality Composer Pro Inspector context menu showing Propagate and Reset options for a prototype entry.](/images/RealityComposerPro/InspectorOverride@2x.png)

**From the Scene Hierarchy:** Control-click an asset, and then select **Reset**, **Propagate**, or **Make Unique**.

![The Reality Composer Pro Scene Hierarchy context menu showing Reset, Propagate, and Make Unique options.](/images/RealityComposerPro/SceneHierarchyComponentContextMenu@2x.png)

#### Change the Prototype Referenced By an Instance

In the Inspector, change the prototype that an instance references.

Select the instance in the Hierarchy. In the Inspector, click the prototype field and select a different prototype from the Project Browser. The instance retains its current overrides, which now apply on top of the new prototype’s values. Remove any overrides that no longer apply to the new prototype.

![A screenshot of the Reality Composer Pro Inspector showing the option to change the prototype that an instance references.](/images/RealityComposerPro/MaterialPrototype@2x.png)

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Explore the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Use Reality Composer Pro’s node-based editor to build materials, animations, audio effects, and scripts without writing code.
- [Previewing content and running simulations](realitycomposerpro-essentials-previewcontentrunsimulations.md)
  Test and iterate on your scenes directly in Reality Composer Pro, with or without a linked Xcode project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-understandingprototypes)*