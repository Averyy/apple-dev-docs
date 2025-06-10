# Specifying a lighting environment in AR Quick Look

**Framework**: ARKit

Add metadata to your USDZ file to specify its lighting characteristics.

#### Overview

AR Quick Look in iOS 16 and later enhances lighting to deliver more brightness, contrast, and visual definition for your scene’s virtual content.

You can set an asset’s lighting environment, or  (IBL), by adding the [`preferredIblVersion`](https://developer.apple.com/documentation/RealityKit/preferrediblversion) metadata to the file’s `.usda` textual definition, or by generating the asset with Apple-provided tools.

##### Set the Lighting Metadata

To define the lighting environment in the asset’s `.usda` textual format using a tool like [`USD Toolset`](https://developer.apple.comhttps://graphics.pixar.com/usd/docs/USD-Toolset.html), add the following metadata:

```None
// asset.usda
#usda 1.0
(
    customLayerData = {
        dictionary Apple = {
            int preferredIblVersion = 2
        }
    }
)
```

A value of `1` indicates the classic lighting environment, and a value of `2` indicates the new lighting environment.

![An image of two 3D assets side by side. On the left, a 3D asset of a biplane toy features shine, refections, and a callout that reads Preferred IBL version = 1. On the right, a 3D asset of the same biplane toy features even more shine and refections, and its callout reads Preferred IBL version = 2.](https://docs-assets.developer.apple.com/published/154637bb579c9c2245cd2aa987caf6a4/media-4107511%402x.png)

If you omit the [`preferredIblVersion`](https://developer.apple.com/documentation/RealityKit/preferrediblversion) metadata or give it a value of `0`, the system checks the asset’s creation timestamp. A timestamp of July 1, 2022, or later results in the new lighting environment; otherwise, the scene features classic lighting for backward compatibility. The system checks the timestamp of the `.usd` asset within the `.usdz` archive, not the archive’s file creation date.

##### Set the Lighting Environment with Apple Provided Tools

With [`Reality Converter`](https://developer.apple.comhttps://developer.apple.com/news/?id=01132020a), you can choose a lighting preferrence for your 3D asset by previewing the available options one after the other. By default, Reality Converter previews an imported 3D asset with `preferrediblversion` = `2`. You can select the Use Classic Lighting option to set `preferrediblversion` to `1` in the file.

![A screenshot of the Reality Converter app displaying a 3D asset of a rocket car in the center pane. In the right pane, the Use Classic Lighting checkbox is selected. A callout for the checkbox reads Preferred IBL version.](https://docs-assets.developer.apple.com/published/2a2dc2f0a5117b63a9695b36dd7abad3/media-4087320%402x.png)

Alternatively, you can use `usdzconvert` in the Apple [`USDZ Tools`](https://developer.apple.comhttps://developer.apple.com/augmented-reality/tools/) suite to output from another file format. Pass an integer value between `0` and `2` for the `--preferrediblversion` argument to add this metadata in the file, as the following example shows:

```swift
usdzconvert fireHydrant.obj --useObjMtl --preferrediblversion 2 
```

##### Match Ar Quick Look Lighting in Third Party Apps and Tools

To design your content in a third-party digital content creation tool (DCC) under the same lighting conditions as AR Quick Look’s lighting environment, configure the tool to use one of the following `.exr` files. Alternatively, you can apply an `.exr` file in your third-party app, such as one that renders with RealityKit, to accommodate the new lighting environment in your app’s runtime experience.

- The [`studio_lighting_objectmode_v002.exr`](https://developer.apple.comhttps://developer.apple.com/sample-code/ar/studio_lighting_objectmode_v002.exr) file provides reflections that match AR Quick Look’s studio object mode. This IBL is appropriate for asset creation in a third-party DCC. Consult the DCC documentation about enabling custom image-based lighting in the tool.
- The [`studio_lighting_armode_v002.exr`](https://developer.apple.comhttps://developer.apple.com/sample-code/ar/studio_lighting_armode_v002.exr) file provides enhanced highlights according to AR Quick Look’s new lighting environment in AR mode. This IBL is appropriate for use in your AR app as a combination with an environment texture that composes captures of the user’s environment. Together, the combination enhances reflections on your app’s virtual content that feature the particular tints and hues of the real world.

![An illustration of object and AR mode reflection pipelines side by side. The left side of the figure depicts the object mode pipeline by extending an arrow from the object mode IBL image to a 3D rendering of a pair of AirPods Max. The AirPods stand upright on a white background and feature light ambient reflections, gloss, and soft shadows commensurate with the look of the object mode IBL. The right side of the figure depicts the AR mode pipeline by displaying the AR mode IBL image above a panorama of a room that’s labeled Environment texture. An image below that combines both images so that the panorama overlays the gloss and highlights of the AR mode IBL image. An arrow extends from that image to a 3D rendering of AirPods Max on top of a camera feed that represents the user’s physical environment. The AirPods rest on a real notebook on a desk. Soft shadows and realistic hues light the AirPods to match the look of the real world while featuring the bright ambiance of the AR mode IBL image.](https://docs-assets.developer.apple.com/published/1086add88f08b9326dc8bfc1a5d6eca6/media-4093141%402x.png)

> 💡 **Tip**:  For apps that render virtual content using RealityKit, set up a skybox with the AR mode IBL to use the new lighting environment. Although AR Quick Look observes the `preferrediblversion` metadata, RealityKit doesn’t. See [`EnvironmentResource`](https://developer.apple.com/documentation/RealityKit/EnvironmentResource) for more information about defining image-based lighting in RealityKit.

## See Also

- [Previewing a Model with AR Quick Look](previewing-a-model-with-ar-quick-look.md)
  Display a model or scene that the user can move, scale, and share with others.
- [Adding Visual Effects in AR Quick Look and RealityKit](adding-visual-effects-in-ar-quick-look-and-realitykit.md)
  Balance the appearance and performance of your AR experiences with modeling strategies.
- [Adding an Apple Pay Button or a Custom Action in AR Quick Look](adding-an-apple-pay-button-or-a-custom-action-in-ar-quick-look.md)
  Provide a banner that users can tap to make a purchase or perform a custom action in an AR experience.
- [USDZ schemas for AR](../RealityKit/usdz-schemas-for-ar.md)
  Add augmented reality functionality to your 3D content using USDZ schemas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/specifying-a-lighting-environment-in-ar-quick-look)*