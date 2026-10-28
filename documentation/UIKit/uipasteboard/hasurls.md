# hasURLs

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL hasURLs;
```

## Discussion

Employ this property to determine if a pasteboard contains URL data.

Do not use the [`url`](./url.md) or [`urls`](./urls.md) properties to determine whether a pasteboard contains URL data, because doing so consumes resources needlessly.

## See Also

### Checking for data types on a pasteboard
- [var hasColors: Bool](./hascolors.md)
  A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [var hasImages: Bool](./hasimages.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [var hasStrings: Bool](./hasstrings.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/hasurls)*