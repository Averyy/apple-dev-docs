# Artwork

**Framework**: Device Management  
**Kind**: dictionary

An object that represents artwork.

**Availability**:
- VPP License Management 2.1+

## Declaration

```swift
object Artwork
```

## Topics

### Related Objects
- [object Artwork.Gradient](artwork/gradient-data.dictionary.md)
  An object that represents the properties of a color gradient for an artwork object.

## Properties

- `assetToken` (string)
- `bgColor` (string): The average background color for the image to use as a placeholder.
- `gradient` (Artwork.Gradient): Gradient information. If absent, use existing gradient behavior. If present, but the body is an empty object {}, then gradient is disabled. This overrides any setting in the editorial item.
- `hasP3` (boolean)
- `height` (number) *(required)*: The largest height available for the source image.
- `pictureFileType` (string)
- `supportsLayeredImage` (boolean)
- `textColor1` (string): A primary text color appropriate to use with the artwork.
- `textColor2` (string): A secondary text color appropriate to use with the artwork.
- `textColor3` (string): An auxiliary text color appropriate to use with the artwork.
- `textColor4` (string): An auxiliary text color appropriate to use with the artwork.
- `url` (string) *(required)*: The URL of the image. May be templated to allow customizing the height {h}, width {w}, and crop code {c}.
- `width` (number) *(required)*: The largest width available for the source image.

## See Also

- [object DescriptionAttribute](descriptionattribute.md)
  An object that represents a description attribute.
- [object Genres](genres.md)
  A resource object that represents a music genre.
- [object Apps](apps.md)
  A resource object that represents an app.
- [object Books](books.md)
  A resource object that represents a book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/artwork)*