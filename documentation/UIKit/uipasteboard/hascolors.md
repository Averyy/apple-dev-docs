# hasColors

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL hasColors;
```

## Discussion

Employ this property to determine if a pasteboard contains color data.

Do not use the [`color`](./color.md) or [`colors`](./colors.md) properties to determine whether a pasteboard contains color data, because doing so consumes resources needlessly.

## See Also

### Checking for data types on a pasteboard
- [var hasImages: Bool](./hasimages.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [var hasStrings: Bool](./hasstrings.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.
- [var hasURLs: Bool](./hasurls.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/hascolors)*