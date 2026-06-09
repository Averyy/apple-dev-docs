# Linking an Xcode project

**Framework**: Reality Composer Pro

Iterate on a scene and run it as an app without leaving the editor.

#### Overview

Linking your Reality Composer Pro project to an [`Xcode`](https://developer.apple.comhttps://developer.apple.com/xcode/) project lets you switch quickly between Reality Composer Pro and Xcode to iterate, preview, simulate, and test your project.

You can iterate on your scene (models, composition, shaders, physics, animation, and game logic) and build and run your app without leaving the editor.

Linking an Xcode project lets you:

- Build and run to devices and simulators.
- Generate an Xcode project directly from Reality Composer Pro using a ready-to-use template.
- Automatically export scene assets to Xcode. Work in Reality Composer Pro and switch to Xcode whenever you need to.

![An annotated demo screenshot showing the Reality Composer Pro and Xcode integration workflow.](https://docs-assets.developer.apple.com/published/27934496e598a666040f0a169decc78b/launchbar%402x.png)

> **Note**: Install Xcode 27 before linking Reality Composer Pro and Xcode projects.

##### Link to a New Xcode Project

1. In the Launch Control toolbar, switch from **Simulate** to **Run with Xcode**.
2. In the toolbar, next to **Run with Xcode**, select **Link an Xcode project**.

![A screenshot of the Reality Composer Pro dialog for choosing options for a new Xcode project — bundle identifier, initial entity, immersive space, and so on.](https://docs-assets.developer.apple.com/published/d36750d794d74e470305177e3a20814d/RunWithXcode-XcodeLaunchBar%402x.png)

1. If you are prompted to install a helper, select **Update**.
2. Choose the options for your Xcode project:

> **Note**: This process generates a Universal app for all platforms that support RealityKit (iOS, iPadOS, macOS, visionOS, and tvOS).

- Organization Identifier
- Bundle Identifier
- Initial Entity (defaults to World)
- Immersive Space - None — Your app runs in a window in the Shared Space on visionOS, or as a standard window on iOS, iPadOS, and macOS.
- Mixed — Your content appears alongside the passthrough view of the user’s surroundings.
- Progressive — Lets the user control how much of their surroundings remains visible.
- Full — Hides passthrough so only your app’s content is visible (fully immersive).

![A screenshot of the Reality Composer Pro Link an Xcode Project dialog.](https://docs-assets.developer.apple.com/published/0e0e899f1225f35acf2b5df864dfeb5f/NewXcodeProject%402x.png)

1. Click **Next**, and then choose a location for your Xcode project.

> **Note**: Reality Composer Pro automatically creates a parent folder to contain your Xcode project.

1. **If** you selected **Include Custom Component**, Reality Composer Pro prompts you to set up your custom component. Click **Yes** to configure them now; otherwise click **Maybe Later**.

##### Link to an Existing Xcode Project

1. In the Launch Control toolbar, switch from **Simulate** to **Run with Xcode**.
2. In the toolbar, next to **Run with Xcode**, select **Link an Xcode project**.
3. Reality Composer Pro prompts you to install a helper. Select **Update**.
4. Click **Link Existing Project**.
5. Click **Next**, and then choose a location for your Xcode project.
6. **If** you selected **Include Custom Component**, Reality Composer Pro prompts you to set up your custom component. Click **Yes** to configure them now; otherwise click **Maybe Later**.
7. After the linking process completes, open your Xcode project, build it, and then restart Reality Composer Pro.

##### Add Custom Components From an Xcode Project

To link an Xcode project with custom plugins — including custom components, custom timeline actions, and custom Script Graph nodes — follow these steps.

1. From the menu bar, choose **Reality Composer Pro** > **Project Settings**.
2. Select **Build Settings**.
3. In the **Plugin Directory** field, enter the folder for your Xcode project. Note that if you are linking a project with custom components, Reality Composer Pro automatically populates this field. Reality Composer Pro links it to the Derived Data path, so you can iterate on your Xcode project code and have your plugins automatically compiled and picked up by Xcode.
4. After you link to an Xcode project, restart Reality Composer Pro to reload the plugins. Reality Composer Pro automatically adds your Xcode project as an available selection in the Add Component list.

##### Preview Content and Run Simulations

You can preview any Reality Composer Pro simulation in the viewport, including physics, VFX, animations, and Script Graphs. This mode is better for content creators — artists, technical artists, and material artists — who want to preview how their scenes or materials look in real time.

While the viewport is convenient for previewing content, sometimes you may want to play the scene in the context of your app, among your SwiftUI views and on a device. For this, you can use the **Run with Xcode** feature.

##### Preview Content on a Connected Device

The Preview on Device feature extends the Reality Composer Pro editor to Apple Vision Pro. Changes you make on the editor can be viewed as real-time previews on the companion Reality Composer Pro app, allowing artists to compose the scene directly on device. The preview connection is local between your Mac and your paired Apple Vision Pro — no scene content leaves your local environment.

1. At the top of Viewport, next to the Play icon, click **Simulate** > **Preview on Device**.
2. Click **Devices**, and then select the device you want to preview on.
3. Click **Play**.

##### Run Simulations for Xcode Linked Projects

Use Run with Xcode to preview your content inside your app, directly from Reality Composer Pro.

After you link an Xcode project, you can preview your Reality Composer Pro project as a compiled application on a connected device or in Simulator.

In the viewport toolbar, click **Running Destinations** and then select a connected device or a simulator.

> **Note**: When building and running to a device, you can track progress from the Launch Control’s status bar or from the Console.

## See Also

- [Configuring the project workspace](realitycomposerpro-essentials-configuringprojectworkspace.md)
  Open a project and arrange the workspace’s tabs and panes to fit your task.
- [Navigating the Reality Composer Pro workspace](realitycomposerpro-essentials-workspaceoverview.md)
  Navigate the panes and toolbars that make up the Reality Composer Pro editing environment.
- [Adding entities and assets to a scene](realitycomposerpro-essentials-addingentitiestoscene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Working with the Graph Editor](realitycomposerpro-essentials-grapheditoroverview.md)
  Add and connect nodes in Reality Composer Pro to create materials, animations, audio effects, scripts, and more.
- [Reusing assets with prototypes and instances](realitycomposerpro-essentials-understandingprototypes.md)
  Reuse a single asset across many scene placements by editing prototypes once and propagating the changes to every instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-linkingxcodeproject)*