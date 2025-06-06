# USDZ schemas for AR

**Framework**: RealityKit

Add augmented reality functionality to your 3D content using USDZ schemas.

#### Overview

Leveraging Pixar’s Universal Scene Description standard, USDZ delivers AR and 3D content to Apple devices. Apple developed a set of new schemas in collaboration with Pixar to further extend the format for AR use cases. Simply add data to a USDZ file to give your 3D assets AR abilities, such as the ability to:

- Anchor 3D content at a specific location in the real world.
- React to real-world situations.
- Participate in a physics simulation.
- Connect audio effects to a location.
- Annotate the environment by displaying text.

A USDZ file uses these schemas to add features to an augmented reality experience in AR Quick Look or [`RealityKit`](RealityKit.md) in place of `.reality` files`,` `.rcproject` files, or custom code to implement AR functionality. Reality Composer describes AR features in its USDZ export using these schemas, too (see `Exporting a Reality Composer Scene to USDZ`). To enable AR features in assets from a third-party digital content-creation (DCC) tool such as Maya or Houdini, edit the file in `.usda` textual format using the [`USD Toolset`](https://developer.apple.comhttps://graphics.pixar.com/usd/docs/USD-Toolset.html).

> **Note**:  These new schemas (see [`Schema definitions for third-party DCCs`](schema-definitions-for-third-party-dccs.md)) are included in the Universal Scene Description specification as an addendum and are marked as preliminary. The addendum also adds metadata (name-value pairs; see [`Metadata`](https://developer.apple.comhttp://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Metadata)), and new data properties ([`Property`](https://developer.apple.comhttp://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Property)). To provide feedback on the addendum, use the [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com/welcome).

 These new schemas (see [`Schema definitions for third-party DCCs`](schema-definitions-for-third-party-dccs.md)) are included in the Universal Scene Description specification as an addendum and are marked as preliminary. The addendum also adds metadata (name-value pairs; see [`Metadata`](https://developer.apple.comhttp://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Metadata)), and new data properties ([`Property`](https://developer.apple.comhttp://graphics.pixar.com/usd/docs/USD-Glossary.html#USDGlossary-Property)). To provide feedback on the addendum, use the [`Feedback Assistant`](https://developer.apple.comhttps://feedbackassistant.apple.com/welcome).

##### Implement Ar Functionality

The following illustration depicts a virtual castle rendered by a , the app or system framework that implements the AR functionality described in the schemas. The prim for the virtual castle (USD refers to individual units of 3D content as  see [`UsdPrim`](https://developer.apple.comhttps://graphics.pixar.com/usd/docs/api/class_usd_prim.html)) instructs the runtime to place the castle on a known image in the physical environment, called the image anchor. When the user comes into proximity with the anchor, the runtime displays the 3D visualization of the castle. Falling snowflakes represent additional prims that behave as if in accordance with gravity, and disappear as they approach a real-world surface.

![An illustration of two tables. On the surface of the table on the left, a two-dimensional image of a castle labeled “image anchor” is outlined by a dotted line to indicate that it is replaceable. The table on the right is the same table, viewed through an AR experience created by the app’s camera pass-through on an iOS device. A virtual castle rests on top of the table in place of the 2D image. Virtual snowflakes descend from virtual clouds to fall around the 3D visualization of the castle. Shadows on the table beneath the snowflakes indicate that the runtime projects the location at which each snowflake will land on the table.](https://docs-assets.developer.apple.com/published/50d3890af48ae074a7c3c96da56ba618/usdz-schemas-for-ar-1%402x.png)

## Topics

### Animation
- [autoPlay](autoplay.md)
  Metadata that specifies whether an animation plays automatically on load.
- [playbackMode](playbackmode.md)
  Metadata that controls animation idling until a behavior takes over.
### Anchoring
- [Placing a prim in the real world](placing-a-prim-in-the-real-world.md)
  Anchor a prim to a real-world object that the runtime recognizes in the physical environment.
- [Preliminary_AnchoringAPI](preliminary-anchoringapi.md)
  A schema that defines the placement of a prim and its children at a real-world location.
- [Preliminary_ReferenceImage](preliminary-referenceimage.md)
  A schema that defines the properties of an image in the physical environment.
### Behaviors
- [Actions and triggers](actions-and-triggers.md)
  Enable visual and audible responses to programmatic or environmental events.
### Text
- [Preliminary_Text](preliminary-text.md)
  A prim that renders 3D text in a scene.
### Scenes and lighting
- [Specifying a lighting environment in AR Quick Look](../ARKit/specifying-a-lighting-environment-in-ar-quick-look.md)
  Add metadata to your USDZ file to specify its lighting characteristics.
- [preferredIblVersion](preferrediblversion.md)
  Metadata that determines the lighting environment of virtual content.
- [sceneLibrary](scenelibrary.md)
  Metadata that partitions an asset into scene-based units.
### Digital content creation
- [Schema definitions for third-party DCCs](schema-definitions-for-third-party-dccs.md)
  Update your local USD library to add interactive and augmented reality features.

## See Also

- [Exporting a Reality Composer Scene to USDZ](exporting-a-reality-composer-scene-to-usdz.md)
  Save a scene or project as USDZ to read, collect, or display in an app or website.
- [Creating USD files for Apple devices](creating-usd-files-for-apple-devices.md)
  Generate 3D assets that render as expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/usdz-schemas-for-ar)*