# Creating a Reality Composer Pro package in your app

**Framework**: Reality Composer Pro

Discover how to add a new or existing Reality Composer Pro project as a package to your app in Xcode.

#### Overview

If you’re building an app for visionOS or using assets in RealityKit, Xcode provides a tool called Reality Composer Pro to help you create and design 3D content. With Reality Composer Pro, you can store your assets in a dedicated Swift package for a more efficient format.

Reality Composer Pro packages can include assets like images, 3D models, audio, and video files. Assets that you add to your Reality Composer Project are stored in the `realitykitcontent.rkassets` bundle, whereas the project’s source code resides in the Sources directory. The package also includes a file called `Package.realitycomposerpro` that contains the Reality Composer Pro project.

> 💡 **Tip**: To improve performance in your app, store all of your RealityKit assets in Reality Composer Pro projects. Loading assets from a Reality Composer Pro project is considerably faster and more resource efficient than loading individual asset files.

##### Create a Visionos Project in Xcode

When you create a visionOS project in Xcode, the editor automatically creates a default Reality Composer Pro project named `RealityKitContent`.

To create a visionOS project in Xcode, choose either App or Immersive Environmental App under the visionOS template tab.

Then fill in the appropriate options for your new project, as shown in the screenshot below:

![A screenshot showcasing an Xcode project options window. The window shows the following options: Project Name, Team, Organization Identifier, Bundle Identifier, Initial Scene Immersive Space Render, and Immersive Space, as well as a check box to include Tests.](https://docs-assets.developer.apple.com/published/e1879d98cbc6170186a90d9604776478/Xcode-NewApp1.png)

The new Xcode project contains two folders in the nagivator area: one with the same name as your app and another called Packages containing the Reality Composer Pro package. The `RealityKitContent` package contains a file called `Package.realitycomposerpro` that you can select to view a 3D visualization of the project in Xcode’s editor area.

![A screenshot of a new Reality Composer Pro project window. The window has a single tab at the top called Example. The window is divided horizontally into two sections. The top section has three views: a navigator view of content in the scene, a viewport in the middle showing a 2D grid, and an inspector view containing details of the scene. The bottom section has four tabs, labeled Project Browser, Shader Graph, Timelines Audio Mixer, and Statistics. Project Browser is currently selected, and it’s also divided into three sections with a navigator on the left showing the project directory, a grid of icons in the middle with Scene.usda selected, and an inspector on the right showing the selected entity hierarchy.](https://docs-assets.developer.apple.com/published/da19a8dda04662f5fe3436f3b8586f54/RCPro-NewProject%402x.png)

You can launch Reality Composer Pro by double-clicking the `Package.realitycomposerpro` file in the navigator. Alternatively, if you have the file selected in the navigator, you can click the Open in Reality Composer Pro button located in the top right corner of the editor area. Double-clicking on any existing `.realitycomposerpro` files launches Reality Composer Pro and opens the selected project.

##### Create a New Reality Composer Pro Package in an Existing Xcode Project

To add a Reality Composer Pro package to an existing Xcode project, you can create a new package with the editor by selecting Xcode > Open Developer Tool > Reality Composer Pro in the menu bar.

![A screenshot of Xcode’s menu bar containing the following options: Xcode, File, Edit, View, Find, Navigate and Editor. The Xcode option is selected, showing a menu with Open Developer Tool selected, opening another menu with Reality Composer Pro selected.](https://docs-assets.developer.apple.com/published/5ce14148e30575d92b974c3bc4492ff5/OpenRCPro-Xcode%402x.png)

In the welcome window for Reality Composer Pro, choose Create New Project.

![A screenshot of the Reality Composer Pro welcome window containing the Reality Composer Pro icon, followed by the title Reality Composer Pro, the current version of the software, Create New Project, Create New Object Capture Model, and Open Existing Project.](https://docs-assets.developer.apple.com/published/12fca2f254fb621e1e7790089030e173/RCPro-WelcomeWindow%402x.png)

Then choose a folder location and name for your Reality Composer Pro project. The project window opens to a new empty scene.

You need to add the package to your Xcode project to use it in your app. In Xcode’s navigation area, Control-click either the Xcode project at the top or a folder underneath it. Choose “Add Files to” in the contextual menu.

![A screenshot of a file’s contextual menu options in Xcode’s navigator view. The option Add Files to iOSTest is highlighted.](https://docs-assets.developer.apple.com/published/42cb76a9e8bd2c9362f521bdbf3db14f/Xcode-AddFiles%402x.png)

Locate the Reality Composer Pro project folder in the pop-up window. Choose the project folder containing the Sources folder, Swift file, and Reality Composer Pro file, and click Add.

![A Finder window showing three items in a folder called Test: a Package.realitycomposerpro file, a Sources folder, and a Package.swift file.](https://docs-assets.developer.apple.com/published/a6a8e4e31760f76642713bb874d45fc0/Xcode-AddProject.png)

You can then either choose to Copy, Move, or Reference the files in place.

The Xcode project’s navigation area now contains the Reality Composer Pro project package and you can use it in your app.

![A screenshot of Xcode’s navigation view for the iOSTest project. A swift package named Untitled is open and a file called Package is highlighted.](https://docs-assets.developer.apple.com/published/92cb56ab6faa67105d7861927e2f34d7/Xcode-ProjectPackage%402x.png)

By default, the code in the `ContentView` loads the 3D Scene from the Reality Composer Pro project into a `RealityView` within the SwiftUI view.

To learn how to load and view a scene from the Reality Composer Pro bundle in your app, see [`Building and running Reality Composer Pro scenes in your app`](build-and-run-reality-composer-pro-scenes-in-your-app.md).

## See Also

- [Configuring the Reality Composer Pro project window](configure-the-reality-composer-pro-project-window.md)
  Change the appearance of the Reality Composer Pro project window by showing and hiding views, and learn to navigate your content.
- [Adding assets to your Reality Composer Pro scene](adding-assets-into-your-reality-composer-pro-scene.md)
  Import assets to design Reality Composer Pro scenes for your app.
- [Building and running Reality Composer Pro scenes in your app](build-and-run-reality-composer-pro-scenes-in-your-app.md)
  Preview scenes on your visionOS device and learn how to load them in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-a-reality-composer-pro-package-in-your-app)*