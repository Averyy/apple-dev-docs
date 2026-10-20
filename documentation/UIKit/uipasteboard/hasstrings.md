# hasStrings

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var hasStrings: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasStrings;
```

#### Discussion

Employ this property to determine if a pasteboard contains string data.

Do not use the [`string`](./string.md) or [`strings`](./strings.md) properties to determine whether a pasteboard contains string data, because doing so consumes resources needlessly.

## See Also

### Checking for data types on a pasteboard
- [var hasColors: Bool](./hascolors.md)
  A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [var hasImages: Bool](./hasimages.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [var hasURLs: Bool](./hasurls.md)
  A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/hasstrings)*