# ratingPlaceholderImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Sets the image used by the rating indicator style in place of the default faded placeholder image.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var ratingPlaceholderImage: NSImage? { get set }
```

```objc
@property (strong, nullable) NSImage * ratingPlaceholderImage;
```

## Discussion

If the custom placeholder is a template image, its fill opacity can be adjusted by modifying the opacity of the template image. If both a [`ratingImage`](./ratingimage.md) and [`ratingPlaceholderImage`](./ratingplaceholderimage.md) are set, each rating position is sized such that either image will fit without scaling (i.e. sized to the maximum width and height of both images). The default value is `nil`.

## See Also

### Managing Placeholder Information
- [var placeholderVisibility: NSLevelIndicator.PlaceholderVisibility](./placeholdervisibility-swift.property.md)
  For a rating-style indicator, sets the conditions under which rating placeholders are displayed.
- [NSLevelIndicator.PlaceholderVisibility](./placeholdervisibility-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/ratingplaceholderimage)*