# contents

**Framework**: SceneKit  
**Kind**: property

The visual contents of the material property—a color, image, or source of animated content. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var contents: Any? { get set }
```

#### Discussion

For details on each visual property and the ways their contents affect a material’s appearance, see [`SCNMaterial`](scnmaterial.md).

You can set a value for this property using any of the following types:

- A color ([`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor)/[`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) or [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor)), specifying a uniform color for the material’s surface
- A number ([`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber)), specifying a uniform scalar value for the material’s surface (useful for physically based properties such as [`metalness`](scnmaterial/metalness.md))
- An image ([`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage)/[`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) or [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage)), specifying a texture to be mapped across the material’s surface
- An [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) or [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object specifying the location of an image file
- A video player ([`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer)) or live video capture preview ([`AVCaptureDevice`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice), in iOS only)
- A Core Animation layer ([`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer))
- A texture ([`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture), [`MDLTexture`](https://developer.apple.com/documentation/ModelIO/MDLTexture), [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture), or [`GLKTextureInfo`](https://developer.apple.com/documentation/GLKit/GLKTextureInfo))
- A SpriteKit scene ([`SKScene`](https://developer.apple.com/documentation/SpriteKit/SKScene))
- A specially formatted image or array of six images, specifying the faces of a cube map

When you examine elements of a scene loaded from a file, this value is always either a color object (of the [`NSColor`](https://developer.apple.com/documentation/AppKit/NSColor) or [`UIColor`](https://developer.apple.com/documentation/UIKit/UIColor) class, according to platform) or an image object (of the [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) or [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) class, according to platform). You can therefore use type introspection (the [`isKind(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isKind(of:)) method in Objective-C, or the `is` operator or `let`-`as` matching in Swift) to determine the type of the material property’s contents.

##### Using Animated Content

In iOS 11, you may use an [`AVCaptureDevice`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice) object to preview live video from a capture device as a material property. In iOS 11, tvOS 11, and macOS 10.13, you may use an [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) object as a material property for video playback.

You may specify any Core Animation layer as the contents of a material property, such as a layer with an animated sublayer hierarchy. SceneKit cannot use a layer that is already being displayed elsewhere (for example, the backing layer of a [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) object).

You can use the SpriteKit framework to provide static or animated content for a material property. SpriteKit provides options for generating and modifying texture images, such as the [`generatingNormalMap()`](https://developer.apple.com/documentation/SpriteKit/SKTexture/generatingNormalMap()) method. You can also use an entire animated SpriteKit scene as the material property’s contents. When you use a [`SKTexture`](https://developer.apple.com/documentation/SpriteKit/SKTexture) object as a material property’s contents, the [`wrapS`](scnmaterialproperty/wraps.md), [`wrapT`](scnmaterialproperty/wrapt.md), [`contentsTransform`](scnmaterialproperty/contentstransform.md), [`minificationFilter`](scnmaterialproperty/minificationfilter.md), [`magnificationFilter`](scnmaterialproperty/magnificationfilter.md) and [`mipFilter`](scnmaterialproperty/mipfilter.md) properties automatically update to match the corresponding features of the SpriteKit texture.

If the current content is a solid color, you can use explicit or implicit animations (see [`Animating SceneKit Content`](animating-scenekit-content.md)) to change to another color, creating an effect that fades between the two colors. Using animations to change from or to other content types results in an instantaneous transition—for an animated transition between textured content types (or types that are themselves animated), create a shader modifier (see [`SCNShadable`](scnshadable.md)).

##### Using Cube Map Texures

SceneKit supports cube maps only for a material’s [`reflective`](scnmaterial/reflective.md) property or for a scene’s [`background`](scnscene/background.md) or [`lightingEnvironment`](scnscene/lightingenvironment.md) property. You can provide a cube map in any of the ways described in Table 1. Of these formats, the vertical strip provides the best performance, because it matches the memory layout SceneKit uses for rendering cube textures.

| Description | Image Size Requirements | Example |
| --- | --- | --- |
| Vertical strip (single image) | height == 6 * width | ![None](https://docs-assets.developer.apple.com/published/67e626c62ce5dc9006447d14e8675026/media-2557196%402x.png) |
| Horizontal strip (single image) | 6 * height == width | ![None](https://docs-assets.developer.apple.com/published/33f655a9f007eb82f86d7e4cc9654d22/media-2557198%402x.png) |
| Spherical projection (single image) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (pixel x/y positions map to latitude/longitude coordinates on a sphere) | 2 * height == width | ![None](https://docs-assets.developer.apple.com/published/f95133aa75bfb4b65a13c9a3f2b2416e/media-2557205%402x.png) |
| Array of six images ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (face order: +X, -X, +Y, -Y, +Z, -Z) | height == width ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) same size for all images | [![None](https://docs-assets.developer.apple.com/published/bb2b1b92be93c0090484c8e5345acf26/media-2557210%402x.png), ![None](https://docs-assets.developer.apple.com/published/daf6f6696d70c8bd445c4bf9b3afdc1a/media-2557212%402x.png), ![None](https://docs-assets.developer.apple.com/published/6004a9da010cab3bbe14463f76ed0bf1/media-2557215%402x.png), ![None](https://docs-assets.developer.apple.com/published/b7531fd4448ab6ff5141e6c5faa1417f/media-2557218%402x.png), ![None](https://docs-assets.developer.apple.com/published/33fbbd2e5f6cac28d55177b86e5eef5e/media-2557221%402x.png), ![None](https://docs-assets.developer.apple.com/published/f4b8d2d7fb470c3a588216a451685186/media-2557226%402x.png)] |

## See Also

- [var intensity: CGFloat](scnmaterialproperty/intensity.md)
  A number between `0.0` and `1.0` that modulates the effect of the material property. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/contents)*