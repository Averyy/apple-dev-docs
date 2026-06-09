# Reusing assets with prototypes and instances

**Framework**: Reality Composer Pro

Reuse a single asset across many scene placements by editing prototypes once and propagating the changes to every instance.

#### Overview

In Reality Composer Pro, a **prototype** is a source asset, and an **instance** is a placement of that prototype in a scene. Dragging the asset into your scene creates a single instance of that prototype. You can place as many instances of the prototype in your scene as you want.

- If you change a prototype, Reality Composer Pro propagates those changes to every instance of that prototype in a scene.
- If you make changes in the Scene Hierarchy to an instance of a prototype, Reality Composer Pro treats the changes as an **Override** on the instance. Overrides don’t affect the prototype itself. Overrides appear in the Scene Hierarchy as a small dot next to the icon.

![A screenshot of the Reality Composer Pro Scene Hierarchy with a white override-indicator dot next to an instance.](https://docs-assets.developer.apple.com/published/b735e828d97e9e869ab6244e58d315ad/SceneHierarchyCropped%402x.png)

##### Work with Prototypes

> ❗ **Important**: Sometimes when you directly assign a prototype to a component, Reality Composer Pro doesn’t automatically create an instance. For example, when you assign a material to a model’s component, any edits to the material directly edit the prototype. To assign an instance of a prototype to the model component instead: 1. In the Project Browser, control-click the material, and then select Instance.
2. Assign the instanced material asset to the model component.

To choose the right action when an instance and its prototype have diverged:

Use **Propagate** when an instance has the look or behavior you want and you want every other instance of the same prototype to match. Propagating from one instance updates the source prototype, which in turn updates every other instance.

Use **Reset** when you’ve experimented with overrides on an instance and want to discard those local edits while keeping the link to the prototype. Reset reverts the instance’s values to the prototype’s; the link stays intact, so future changes to the prototype still flow through.

Use **Make Unique** when an instance has diverged enough that it should no longer track the prototype at all. Make Unique severs the prototype link, leaving a standalone copy that doesn’t receive future propagated changes.

You can take these actions from either the Inspector or the Scene Hierarchy.

##### From the Inspector

In the **Inspector**, control-click the entry you want to change, and then select one of the following:

- **Propagate** — Propagates changes to the prototype. This affects every instance of that prototype in your project.
- **Reset** — Undoes all changes and resets the prototype to its original state.

![The Reality Composer Pro Inspector context menu showing Propagate and Reset options for a prototype entry.](https://docs-assets.developer.apple.com/published/2e5889613ad3ef33b84a85cd5dd34d54/InspectorOverride%402x.png)

##### From the Scene Hierarchy

You can also change overrides from the Scene Hierarchy. Control-click an asset, and then select one of the following:

- **Reset** — Removes the override for the selected asset, undoing local edits. Apply Reset to an instance whose properties have been changed from its prototype. This discards your local edits and reverts the values to the prototype’s, while keeping the prototype link intact.
- **Propagate** — Propagates changes to the source prototype. This affects every instance of that prototype in your project.
- **Make Unique** — Removes the link to the prototype and converts the instance into a standalone copy. The new copy retains the instance’s current values but no longer receives changes propagated from the original prototype.

![The Reality Composer Pro Scene Hierarchy context menu showing Reset, Propagate, and Make Unique options.](https://docs-assets.developer.apple.com/published/b36bdbc0a77bc229562f7fbae33f39aa/SceneHierarchyComponentContextMenu%402x.png)

##### Change the Prototype an Instance References

In the Inspector, you can also change the prototype that an instance is referencing.

![A screenshot of the Reality Composer Pro Inspector showing the option to change the prototype that an instance references.](https://docs-assets.developer.apple.com/published/0b6159a449e770c10894029cd0993985/MaterialPrototype%402x.png)

## See Also

- [Linking an Xcode project](realitycomposerpro-essentials-linkingxcodeproject.md)
  Iterate on a scene and run it as an app without leaving the editor.
- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Navigate the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Add and connect nodes in Reality Composer Pro to create materials, animations, audio effects, scripts, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-understandingprototypes)*