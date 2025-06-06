# hasURLs

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hasURLs: Bool { get }
```

#### Discussion

Employ this property to determine if a pasteboard contains URL data.

Do not use the [`url`](uipasteboard/url.md) or [`urls`](uipasteboard/urls.md) properties to determine whether a pasteboard contains URL data, because doing so consumes resources needlessly.

## See Also

- [var hasColors: Bool](uipasteboard/hascolors.md)
  A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [var hasImages: Bool](uipasteboard/hasimages.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [var hasStrings: Bool](uipasteboard/hasstrings.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/hasurls)*