# hasImages

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the pasteboard contains a nonempty array of images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hasImages: Bool { get }
```

#### Discussion

Employ this property to determine if a pasteboard contains image data.

Do not use the [`image`](uipasteboard/image.md) or [`images`](uipasteboard/images.md) properties to determine whether a pasteboard contains image data, because doing so consumes resources needlessly.

## See Also

- [var hasColors: Bool](uipasteboard/hascolors.md)
  A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [var hasStrings: Bool](uipasteboard/hasstrings.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.
- [var hasURLs: Bool](uipasteboard/hasurls.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/hasimages)*