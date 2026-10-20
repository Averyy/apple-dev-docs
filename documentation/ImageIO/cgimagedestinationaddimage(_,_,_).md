# CGImageDestinationAddImage(_:_:_:)

**Framework**: Image I/O  
**Kind**: func  
**Role**: Function

Adds an image to an image destination.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGImageDestinationAddImage(_ idst: CGImageDestination, _ image: CGImage, _ properties: CFDictionary?)
```

```c
extern void CGImageDestinationAddImage(CGImageDestinationRef idst, CGImageRef image, CFDictionaryRef properties);
```

#### Discussion

The function logs an error if you add more images than what you specified when you created the image destination.

## Parameters

- `idst`: The image destination to modify.
- `image`: The image to add.
- `properties`: An optional dictionary that specifies the properties of the added image. Specify `NULL` to omit any additional properties. For a list of possible values, see [Image Properties](./image-properties.md) and doc:CGImageDestination/Configuring-the-Image-Behaviors.

## See Also

### Adding Images to the Destination
- [func CGImageDestinationAddImageFromSource(CGImageDestination, CGImageSource, Int, CFDictionary?)](./cgimagedestinationaddimagefromsource%28_,_,_,_%29.md)
  Adds an image from an image source to an image destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationaddimage(_:_:_:))*