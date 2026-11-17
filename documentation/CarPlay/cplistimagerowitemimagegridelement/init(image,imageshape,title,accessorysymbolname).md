# init(image:imageShape:title:accessorySymbolName:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a row element with the specified image, text, and attributes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(image: UIImage, imageShape: CPListImageRowItemImageGridElement.Shape, title: String, accessorySymbolName: String?)
```

```objc
- (instancetype) initWithImage:(UIImage *) image imageShape:(CPListImageRowItemImageGridElementShape) imageShape title:(NSString *) title accessorySymbolName:(NSString *) accessorySymbolName;
```

## Return Value

An initialized element you can add to a row.

## Parameters

- `image`: The image to display as the element’s primary content. If the image originates from an asset catalog, CarPlay manages the light and dark variants of your image and switches them when needed. Specify images with the dimensions listed in the [`maximumImageSize`](../cplistimagerowitemcardelement/maximumimagesize.md) property. If your image is smaller or larger than the maximum dimensions, CarPlay scales the image as needed to fit the space. Don’t specify an image object with an animated sequence of images.
- `imageShape`: The shape to apply to `image`.
- `title`: The primary text to display beneath the image. CarPlay displays this string with a visually prominent style.
- `accessorySymbolName`: The name of an image to display next to the title. Specify the name of an SF Symbol or the name of a custom image resource in your app’s main bundle. Specify `nil` to omit this image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemimagegridelement/init(image:imageshape:title:accessorysymbolname:))*