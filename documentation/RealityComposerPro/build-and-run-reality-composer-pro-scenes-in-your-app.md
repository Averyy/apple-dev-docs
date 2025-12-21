# Building and running Reality Composer Pro scenes in your app

**Framework**: Reality Composer Pro

Preview scenes on your visionOS device and learn how to load them in your app.

#### Overview

During development, your Reality Composer Pro projects change over time and may get more complex. You can preview your scene directly in Reality Composer Pro on a visionOS device without having to build and run in Xcode. If you’re ready to test how your content runs in your app, you can build and run your app with either Xcode’s visionOS simulator or on a physical device.

##### Preview Scenes on a Device

If you have an Apple Vision Pro connected to your Mac, you can preview your scene on the device by selecting Preview > Play on the menu bar or by clicking on the Preview button in the Reality Composer Pro toolbar, represented by an Apple Vision Pro icon. If you have multiple Apple Vision Pro devices connected, choose which device to use by clicking the menu next to the Preview button.

##### Load Scenes in Your Apps View

You can load a Reality Composer Pro scene similar to how you load a `.usdz` asset from your app bundle. The difference is you have to specify the Reality Composer Pro package bundle instead. You can do this in the `make` closure of a [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView) initializer.

Each Reality Composer Pro package defines a global constant that points to its bundle. The system creates the bundle name by appending “Bundle” to the end of the project’s name.

In the default visionOS template in Xcode, the Reality Composer Pro project is called `RealityKitContent`, with the global bundle variable called `realityKitContentBundle`. The following code shows how to load the default bundle into a `RealityView`:

```swift
    RealityView { content in
        if let scene = try? await Entity.load(named: "Biplane", 
            in: realityKitContentBundle) {
                myDataModel.add(scene) 
                content.add(scene)
                } update: { content in
                    // ...
                    }
    }
```

> **Note**: The code example above saves a reference to the root node. This isn’t required, but with [`RealityView`](https://developer.apple.com/documentation/RealityKit/RealityView), you don’t have ready access to the scene content, unlike [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView) on iOS and macOS. It’s best to maintain your own reference to the root entity of your scene in your app’s data model.

When RealityKit finishes loading the scene, the `scene` variable contains the root entity of the specified scene and includes this content in `content`, which is then displayed by `RealityView` to the user.

##### Run the App with the Reality Composer Pro Project

To build and run your Xcode project, choose Product > Run, or click the Run button in your project’s toolbar. You can test your app’s performance with either the visionOS simulator or a connected physical device.

## See Also

- [Creating a Reality Composer Pro package in your app](creating-a-reality-composer-pro-package-in-your-app.md)
  Discover how to add a new or existing Reality Composer Pro project as a package to your app in Xcode.
- [Configuring the Reality Composer Pro project window](configure-the-reality-composer-pro-project-window.md)
  Change the appearance of the Reality Composer Pro project window by showing and hiding views, and learn to navigate your content.
- [Adding assets to your Reality Composer Pro scene](adding-assets-into-your-reality-composer-pro-scene.md)
  Import assets to design Reality Composer Pro scenes for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/build-and-run-reality-composer-pro-scenes-in-your-app)*