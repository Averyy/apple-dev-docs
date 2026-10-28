# init(image:)

**Framework**: SpriteKit  
**Kind**: init  
**Role**: Initializer

Create a new texture object from an image object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
convenience init(image: UIImage)
```

*macOS*

```swift
convenience init(image: NSImage)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
+ (instancetype) textureWithImage:(UIImage *) image;
```

*macOS*

```objc
+ (instancetype) textureWithImage:(NSImage *) image;
```

## Return Value

A new texture object.

## Discussion

The image data is copied before control is returned to your game.

## Parameters

- `image`: An image.

## See Also

### Texture from Image
- [convenience init(cgImage: CGImage)](./init%28cgimage%29-27ovb.md)
  Create a new texture object from a Quartz 2D image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/init(image:))*