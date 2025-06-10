# preferredIblVersion

**Framework**: RealityKit

Metadata that determines the lighting environment of virtual content.

#### Overview

This metadata selects one of two predefined options for the scene’s image-based lighting (IBL). AR Quick Look in iOS 16 and later observes this property to enhance the brightness, contrast, and visual definition of a scene’s virtual content.

A value of `1` indicates the classic lighting environment, and a value of `2` indicates the new lighting environment.

![An image of two 3D assets side by side. On the left, a 3D asset of a biplane toy features shine, refections, and a callout that reads Preferred IBL version = 1. On the right, a 3D asset of the same biplane toy features even more shine and refections, and its callout reads Preferred IBL version = 2.](https://docs-assets.developer.apple.com/published/154637bb579c9c2245cd2aa987caf6a4/media-4107512.png)

If you omit the [`preferredIblVersion`](preferrediblversion.md) metadata or give it a value of `0`, the system checks the asset’s creation timestamp. A timestamp of July 1, 2022, or later results in the new lighting environment; otherwise, the scene features classic lighting for backward compatibility. The system checks the timestamp of the `.usd` asset within the `.usdz` archive, not the archive’s file creation date.

##### Declaration

```other
int preferredIblVersion = 0
```

##### Select the Scenes Image Based Lighting

The following `.usda` definition chooses the new lighting environment:

```other
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

> 💡 **Tip**: RealityKit doesn’t observe the [`preferredIblVersion`](preferrediblversion.md) metadata, but you configure the same lighting environment manually. See [`Specifying a lighting environment in AR Quick Look`](https://developer.apple.com/documentation/ARKit/specifying-a-lighting-environment-in-ar-quick-look) for more information about matching AR Quick Look’s lighting environment in RealityKit apps.

## See Also

- [Specifying a lighting environment in AR Quick Look](../ARKit/specifying-a-lighting-environment-in-ar-quick-look.md)
  Add metadata to your USDZ file to specify its lighting characteristics.
- [sceneLibrary](scenelibrary.md)
  Metadata that partitions an asset into scene-based units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/preferrediblversion)*