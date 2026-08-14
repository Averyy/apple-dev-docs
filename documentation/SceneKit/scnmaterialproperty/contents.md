# contents

**Framework**: SceneKit  
**Kind**: property

The visual contents of the material property—a color, image, or source of animated content. Animatable.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var contents: Any? { get set }
```

#### Discussion

For details on each visual property and the ways their contents affect a material’s appearance, see [`SCNMaterial`](scnmaterial.md).

You can set a value for this property using any of the following types:

- A color ([`NSColor`](https://developer.apple.com/documentation/appkit/nscolor)/[`UIColor`](https://developer.apple.com/documentation/uikit/uicolor) or [`CGColor`](https://developer.apple.com/documentation/coregraphics/cgcolor)), specifying a uniform color for the material’s surface
- A number ([`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber)), specifying a uniform scalar value for the material’s surface (useful for physically based properties such as [`metalness`](scnmaterial/metalness.md))
- An image ([`NSImage`](https://developer.apple.com/documentation/appkit/nsimage)/[`UIImage`](https://developer.apple.com/documentation/uikit/uiimage) or [`CGImage`](https://developer.apple.com/documentation/coregraphics/cgimage)), specifying a texture to be mapped across the material’s surface
- An [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) or [`NSURL`](https://developer.apple.com/documentation/foundation/nsurl) object specifying the location of an image file
- A video player ([`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer)) or live video capture preview ([`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice), in iOS only)
- A Core Animation layer ([`CALayer`](https://developer.apple.com/documentation/quartzcore/calayer))
- A texture ([`SKTexture`](https://developer.apple.com/documentation/spritekit/sktexture), [`MDLTexture`](https://developer.apple.com/documentation/modelio/mdltexture), [`MTLTexture`](https://developer.apple.com/documentation/metal/mtltexture), or [`GLKTextureInfo`](https://developer.apple.com/documentation/glkit/glktextureinfo))
- A SpriteKit scene ([`SKScene`](https://developer.apple.com/documentation/spritekit/skscene))
- A specially formatted image or array of six images, specifying the faces of a cube map

When you examine elements of a scene loaded from a file, this value is always either a color object (of the [`NSColor`](https://developer.apple.com/documentation/appkit/nscolor) or [`UIColor`](https://developer.apple.com/documentation/uikit/uicolor) class, according to platform) or an image object (of the [`NSImage`](https://developer.apple.com/documentation/appkit/nsimage) or [`UIImage`](https://developer.apple.com/documentation/uikit/uiimage) class, according to platform). You can therefore use type introspection (the [`isKind(of:)`](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/iskind(of:)) method in Objective-C, or the `is` operator or `let`-`as` matching in Swift) to determine the type of the material property’s contents.

##### Using Animated Content

In iOS 11, you may use an [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice) object to preview live video from a capture device as a material property. In iOS 11, tvOS 11, and macOS 10.13, you may use an [`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer) object as a material property for video playback.

You may specify any Core Animation layer as the contents of a material property, such as a layer with an animated sublayer hierarchy. SceneKit cannot use a layer that is already being displayed elsewhere (for example, the backing layer of a [`UIView`](https://developer.apple.com/documentation/uikit/uiview) object).

You can use the SpriteKit framework to provide static or animated content for a material property. SpriteKit provides options for generating and modifying texture images, such as the [`generatingNormalMap()`](https://developer.apple.com/documentation/spritekit/sktexture/generatingnormalmap()) method. You can also use an entire animated SpriteKit scene as the material property’s contents. When you use a [`SKTexture`](https://developer.apple.com/documentation/spritekit/sktexture) object as a material property’s contents, the [`wrapS`](scnmaterialproperty/wraps.md), [`wrapT`](scnmaterialproperty/wrapt.md), [`contentsTransform`](scnmaterialproperty/contentstransform.md), [`minificationFilter`](scnmaterialproperty/minificationfilter.md), [`magnificationFilter`](scnmaterialproperty/magnificationfilter.md) and [`mipFilter`](scnmaterialproperty/mipfilter.md) properties automatically update to match the corresponding features of the SpriteKit texture.

If the current content is a solid color, you can use explicit or implicit animations (see [`Animating SceneKit Content`](animating-scenekit-content.md)) to change to another color, creating an effect that fades between the two colors. Using animations to change from or to other content types results in an instantaneous transition—for an animated transition between textured content types (or types that are themselves animated), create a shader modifier (see [`SCNShadable`](scnshadable.md)).

##### Using Cube Map Texures

SceneKit supports cube maps only for a material’s [`reflective`](scnmaterial/reflective.md) property or for a scene’s [`background`](scnscene/background.md) or [`lightingEnvironment`](scnscene/lightingenvironment.md) property. You can provide a cube map in any of the ways described in Table 1. Of these formats, the vertical strip provides the best performance, because it matches the memory layout SceneKit uses for rendering cube textures.

| Description | Image Size Requirements | Example |
| --- | --- | --- |
| Vertical strip (single image) | height == 6 * width | ![None](/images/com.apple.scenekit/media-2557196@2x.png) |
| Horizontal strip (single image) | 6 * height == width | ![None](/images/com.apple.scenekit/media-2557198@2x.png) |
| Spherical projection (single image) ![None](/images/com.apple.scenekit/spacer.png) (pixel x/y positions map to latitude/longitude coordinates on a sphere) | 2 * height == width | ![None](/images/com.apple.scenekit/media-2557205@2x.png) |
| Array of six images ![None](/images/com.apple.scenekit/spacer.png) (face order: +X, -X, +Y, -Y, +Z, -Z) | height == width ![None](/images/com.apple.scenekit/spacer.png) same size for all images | [![None](/images/com.apple.scenekit/media-2557210@2x.png), ![None](/images/com.apple.scenekit/media-2557212@2x.png), ![None](/images/com.apple.scenekit/media-2557215@2x.png), ![None](/images/com.apple.scenekit/media-2557218@2x.png), ![None](/images/com.apple.scenekit/media-2557221@2x.png), ![None](/images/com.apple.scenekit/media-2557226@2x.png)] |

## See Also

- [var intensity: CGFloat](scnmaterialproperty/intensity.md)
  A number between `0.0` and `1.0` that modulates the effect of the material property. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/contents)*