# placeholderVisibility

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

For a rating-style indicator, sets the conditions under which rating placeholders are displayed.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var placeholderVisibility: NSLevelIndicator.PlaceholderVisibility { get set }
```

```objc
@property NSLevelIndicatorPlaceholderVisibility placeholderVisibility;
```

#### Discussion

This property currently has no effect for other indicator styles. The default value is `NSLevelIndicatorPlaceholderVisibilityAutomatic`.

## See Also

### Managing Placeholder Information
- [var ratingPlaceholderImage: NSImage?](./ratingplaceholderimage.md)
  Sets the image used by the rating indicator style in place of the default faded placeholder image.
- [NSLevelIndicator.PlaceholderVisibility](./placeholdervisibility-swift.enum.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslevelindicator/placeholdervisibility-swift.property)*