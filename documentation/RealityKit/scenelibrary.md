# sceneLibrary

**Framework**: RealityKit

Metadata that partitions an asset into scene-based units.

#### Overview

Set a prim’s `kind` metadata to `sceneLibrary` to create a  Partitioning an asset’s contents into multiple scenes offers the following benefits:

- Prims segment content into distinct parts that have differing utilities and lifetimes.
- Unlike USD [`Variant Sets`](https://developer.apple.comhttps://graphics.pixar.com/usd/docs/Authoring-Variants.html), you can mark each scene active or inactive independently.
- Actions can operate on scenes.

The runtime doesn’t support multiple active scenes in a single file. When a USDZ file loads, the runtime displays the first active scene. The runtime ignores nested scenes. If an asset doesn’t define a scene, the runtime loads the full file contents as a single scene.

Define a scene using the `def` keyword to specify the asset’s active scene –– that is, the one that the runtime makes visible on load. Use the `over` keyword to specify inactive scenes –– those that are invisible on load. The runtime doesn’t display inactive scenes. The advantage of inactive scenes is that you can activate one in an editor during development, and an app can transition to an inactive scene during the AR experience.

This specification is backward compatible because of the way traditional USD runtimes skip `over` definitions. A runtime that doesn’t support the `sceneLibrary` metadata displays only the first active scene.

##### Declaration

```other
kind = "sceneLibrary"
```

##### Partition Content Into Scenes

The following example demonstrates a scene template on which you can base your asset.

```other
def Xform "Root" (
    # Because you can apply `kind` to any type of prim, that allows any prim to be a scene.
    kind = "sceneLibrary"
)
{
    # `PrimaryScene` is immediately active due to the `def` keyword.
    def Xform "PrimaryScene" (
        # `sceneName` can be any human-readable string.
        sceneName = "Primary Scene"
    )
    {
    }

    # `SecondaryScene` is inactive due to the over keyword.
    over Xform "SecondaryScene" (
        sceneName = "Secondary Scene"
    )
    {
    }
}

```

Use the `sceneName` property to refer to a scene to load it or transition to it from another scene.

## See Also

- [Specifying a lighting environment in AR Quick Look](../ARKit/specifying-a-lighting-environment-in-ar-quick-look.md)
  Add metadata to your USDZ file to specify its lighting characteristics.
- [preferredIblVersion](preferrediblversion.md)
  Metadata that determines the lighting environment of virtual content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scenelibrary)*