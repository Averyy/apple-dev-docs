# init(image:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a grid row element with the specified image.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(image: UIImage)
```

```objc
- (instancetype) initWithImage:(UIImage *) image;
```

## Return Value

An initialized element you can add to a row.

## Discussion

This method stores a copy of `image` in the inherited [`image`](../cplistimagerowitemelement/image.md) property.

## Parameters

- `image`: The image to display as the element’s primary content. If the image originates from an asset catalog, CarPlay manages the light and dark variants of your image and switches them when needed. Specify images with the dimensions listed in the [`maximumImageSize`](../cplistimagerowitemcardelement/maximumimagesize.md) property. If your image is smaller or larger than the maximum dimensions, CarPlay scales the image to fit the space. Don’t specify an image object with an animated sequence of images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemgridelement/init(image:))*