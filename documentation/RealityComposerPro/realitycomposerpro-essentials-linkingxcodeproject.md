# Linking an Xcode project

**Framework**: Reality Composer Pro

Iterate on a scene and run it as an app without leaving the editor.

#### Overview

Linking your Reality Composer Pro project to an [`Xcode`](https://developer.apple.comhttps://developer.apple.com/xcode/) project lets you switch quickly between Reality Composer Pro and Xcode to iterate, preview, simulate, and test your project. With this connection, you can build and run to devices and simulators, automatically export scene assets to Xcode as you work, and generate a ready-to-use Xcode project template.

You can also iterate on your scene (models, composition, shaders, physics, animation, and game logic) and build and run your app without leaving the editor. For more information about previewing content and running simulations, see [`Previewing content and running simulations`](realitycomposerpro-essentials-previewcontentrunsimulations.md).

![An annotated demo screenshot showing the Reality Composer Pro and Xcode integration workflow.](/images/RealityComposerPro/launchbar@2x.png)

> **Note**: Install Xcode 27 before linking Reality Composer Pro and Xcode projects.

#### Link to a New Xcode Project

To link to a new Xcode project, do the following:

1. In the Launch Control toolbar, switch from **Simulate** to **Run with Xcode**.
2. In the toolbar, next to **Run with Xcode**, select **Link an Xcode project**.

![A screenshot of the Reality Composer Pro dialog for choosing options for a new Xcode project — bundle identifier, initial entity, immersive space, and so on.](/images/RealityComposerPro/RunWithXcode-XcodeLaunchBar@2x.png)

1. If you are prompted to install a helper, select **Update**.
2. Choose the options for your Xcode project:

> **Note**: This process generates a Universal app for all platforms that support RealityKit (iOS, iPadOS, macOS, visionOS, and tvOS).

- Organization Identifier
- Bundle Identifier
- Initial Entity (defaults to World)
- Immersive Space - None — Your app runs in a window in the Shared Space on visionOS, or as a standard window on iOS, iPadOS, and macOS.
- Mixed — Your content appears alongside the passthrough view of your surroundings.
- Progressive — Lets you control how much of your surroundings remains visible.
- Full — Shows only your app’s content (fully immersive).

![A screenshot of the Reality Composer Pro Link an Xcode Project dialog.](/images/RealityComposerPro/NewXcodeProject@2x.png)

1. Click **Next**, and then choose a location for your Xcode project.

> **Note**: Reality Composer Pro automatically creates a parent folder to contain your Xcode project.

1. **If** you selected **Include Custom Component**, Reality Composer Pro prompts you to set up your custom component. Click **Yes** to configure them now; otherwise click **Maybe Later**.

#### Link to an Existing Xcode Project

1. In the Launch Control toolbar, switch from **Simulate** to **Run with Xcode**.
2. In the toolbar, next to **Run with Xcode**, select **Link an Xcode project**.
3. Reality Composer Pro prompts you to install a helper. Select **Update**.
4. Click **Link Existing Project**.
5. Click **Next**, and then choose a location for your Xcode project.
6. **If** you selected **Include Custom Component**, Reality Composer Pro prompts you to set up your custom component. Click **Yes** to configure them now; otherwise click **Maybe Later**.
7. After the linking process completes, open your Xcode project, build it, and then restart Reality Composer Pro.

#### Add Custom Components From an Xcode Project

To link an Xcode project with custom plugins — including custom components, custom timeline actions, and custom Script Graph nodes — follow these steps.

1. From the menu bar, choose **Reality Composer Pro** > **Project Settings**.
2. Select **Build Settings**.
3. In the **Plugin Directory** field, enter the folder for your Xcode project. Note that if you are linking a project with custom components, Reality Composer Pro automatically populates this field. Reality Composer Pro links it to the Derived Data path, so you can iterate on your Xcode project code and have your plugins automatically compiled and picked up by Xcode.
4. After you link to an Xcode project, restart Reality Composer Pro to reload the plugins. Reality Composer Pro automatically adds your Xcode project as an available selection in the Add Component list.

## See Also

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
- [Previewing content and running simulations](realitycomposerpro-essentials-previewcontentrunsimulations.md)
  Test and iterate on your scenes directly in Reality Composer Pro, with or without a linked Xcode project.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/realitycomposerpro-essentials-linkingxcodeproject)*