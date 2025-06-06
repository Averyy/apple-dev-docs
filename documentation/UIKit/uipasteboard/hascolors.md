# hasColors

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hasColors: Bool { get }
```

#### Discussion

Employ this property to determine if a pasteboard contains color data.

Do not use the [`color`](uipasteboard/color.md) or [`colors`](uipasteboard/colors.md) properties to determine whether a pasteboard contains color data, because doing so consumes resources needlessly.

## See Also

- [var hasImages: Bool](uipasteboard/hasimages.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [var hasStrings: Bool](uipasteboard/hasstrings.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.
- [var hasURLs: Bool](uipasteboard/hasurls.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/hascolors)*