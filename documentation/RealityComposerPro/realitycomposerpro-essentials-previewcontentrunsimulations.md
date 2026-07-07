# Previewing content and running simulations

**Framework**: Reality Composer Pro

Test and iterate on your scenes directly in Reality Composer Pro, with or without a linked Xcode project.

#### Overview

Reality Composer Pro lets you preview or simulate content on both real and virtual devices, with or without a linked Xcode project. You can iterate on your scene and build and run your app without leaving the editor.

![An annotated demo screenshot showing the Reality Composer Pro and Xcode integration workflow.](https://docs-assets.developer.apple.com/published/27934496e598a666040f0a169decc78b/launchbar%402x.png)

The Preview tab shows a preview of the currently selected entity you are working on. For example, you can preview any Reality Composer Pro entity in a simulated visionOS or Mac environment — this mode is suited for content creators who want to preview how their scenes look in real time. To test a scene with actual interactions, views, cameras, game controllers, and live code on a real or simulated device, you need to link your Xcode project first. See [`Linking an Xcode project`](realitycomposerpro-essentials-linkingxcodeproject.md) to learn how.

#### Run Simulations in the Reality Composer Pro Viewport

At the top of the Viewport, next to the Play icon, click **Simulate** to view a simulation in the Viewport.

#### Preview Content on a Connected Device

At the top of the Viewport, next to the Play icon, click **Simulate** > **Preview on Device**. Then click **Devices** and select the device you want to preview on. If you need to connect an Apple Vision Pro, select **Download Reality Composer Pro Preview for visionOS**, then click **Play**.

#### Run Simulations for Xcode Linked Projects

Once you have successfully linked an Xcode project, you can use Reality Composer Pro’s Simulator to preview your Xcode and Reality Composer Pro project as a compiled application on either a connected physical device or a simulated device.

Above the Viewport, click **Running Destinations** and then select a connected device or a simulated device.

> **Note**: The first time you do this, it may take some time for the project to compile. Subsequent simulations for the same device compile and run faster.

#### Load Scenes in Your Apps View

You can load a Reality Composer Pro scene the same way you load a `.usdz` asset from your app bundle. Specify the Reality Composer Pro package bundle instead, in the `make` closure of a [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) initializer.

Each Reality Composer Pro package defines a global constant that points to its bundle. The system creates the bundle name by appending “Bundle” to the end of the project’s name.

Xcode’s default visionOS template names the Reality Composer Pro project `RealityKitContent` and the global bundle variable `realityKitContentBundle`. The following code shows how to load the default bundle into a `RealityView`:

```swift
RealityView { content in
    if let scene = try? await Entity(named: "Biplane",
        in: realityKitContentBundle) {
        myDataModel.add(scene)
        content.add(scene)
    }
} update: { content in
    // ...
}
```

> **Note**: The code example above saves a reference to the root node. This isn’t required, but with `RealityView`, you don’t have ready access to the scene content — unlike `ARView` on iOS and macOS, which exposes scene content through its `scene` property. Maintain your own reference to the root entity of your scene in your app’s data model.

When RealityKit finishes loading the scene, the `scene` variable contains the root entity of the specified scene. `RealityView` adds this entity to `content` and displays it to the user.

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
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Edit a prototype once and propagate the change to every placement of that asset in a scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-previewcontentrunsimulations)*