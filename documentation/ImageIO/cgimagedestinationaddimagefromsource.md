# CGImageDestinationAddImageFromSource(_:_:_:_:)

**Framework**: Image I/O  
**Kind**: func

Adds an image from an image source to an image destination.

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
func CGImageDestinationAddImageFromSource(_ idst: CGImageDestination, _ isrc: CGImageSource, _ index: Int, _ properties: CFDictionary?)
```

## Parameters

- `idst`: The image destination to modify.
- `isrc`: An image source that contains the image.
- `index`: The index of the image in the image source. Specify a valid, zero-based index into the images of the image source. If the index is invalid, this method returns  .
- `properties`: An optional dictionary that specifies additional image property information. The added image automatically inherits the properties found in the image source. Use this dictionary to add properties to the image, or to modify one of the inherited properties. To remove an inherited property altogether, specify   for the property’s value. For a list of possible values, see   and  .

## See Also

- [func CGImageDestinationAddImage(CGImageDestination, CGImage, CFDictionary?)](cgimagedestinationaddimage(_:_:_:).md)
  Adds an image to an image destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageio/cgimagedestinationaddimagefromsource(_:_:_:_:))*