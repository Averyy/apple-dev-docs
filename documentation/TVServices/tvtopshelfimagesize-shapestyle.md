# TVTopShelfImageSize(shape:style:)

**Framework**: TV Services  
**Kind**: func

Returns the ideal size for an image, according to its particular shape and style.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
func TVTopShelfImageSize(shape: TVContentItemImageShape, style: TVTopShelfContentStyle) -> CGSize
```

#### Discussion

Call this function to determine the ideal image size to use to avoid image scaling. Typically, if your app has access to multiple images for a given piece of content, you use this function to choose which image most closely matches the ideal size for the version of the operating system that your app is running on. An image provided in that size does not require any image scaling. If you request the size of a shape that is not allowed in the given style, the function returns [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero).

## Parameters

- `shape`: The shape of the content item.
- `style`: The style of the TV Top Shelf user interface.

## See Also

- [class TVContentItem](tvcontentitem.md)
  An object that describes either a piece of content or a container for other content items.
- [class TVContentIdentifier](tvcontentidentifier.md)
  An object that uniquely identifies media content in either a single piece or a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfimagesize(shape:style:))*