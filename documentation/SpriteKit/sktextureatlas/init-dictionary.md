# init(dictionary:)

**Framework**: SpriteKit  
**Kind**: init

Creates a texture atlas from a set of image files.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
convenience init(dictionary properties: [String : Any])
```

## Mentions

- [About Texture Atlases](about-texture-atlases.md)

#### Return Value

A new texture atlas object.

#### Discussion

Normally, Xcode creates texture atlases at compile time from the image files included in your project. These atlases are compiled and installed inside the app bundle. However, sometimes the assets needed to create a texture atlas are not available at compile time. For example, those assets might be procedurally generated or downloaded from the network. However, you still want the benefit of texture atlases to reduce the number of state changes required in the hardware. You can use this method to generate an atlas object at runtime. This is a potentially expensive operation best performed when your game loop is not running.

The keys in the dictionary represent the names of the individual textures. The associated object for each key can be:

- An [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object that contains a file system path to a file that contains the texture
- An [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) object that contains a file system path to a file that contains the texture
- A [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) object
- An [`NSImage`](https://developer.apple.com/documentation/AppKit/NSImage) object

## Parameters

- `properties`: A dictionary that defines which textures are to be merged into the atlas.

## See Also

- [convenience init(named: String)](sktextureatlas/init(named:).md)
  Creates a texture atlas from data stored in the app bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktextureatlas/init(dictionary:))*