# largeContentTitle

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A string that describes an item to display in the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var largeContentTitle: String? { get }
```

#### Discussion

To present content in the large content viewer, you can provide either [`largeContentTitle`](uilargecontentvieweritem/largecontenttitle.md) or [`largeContentImage`](uilargecontentvieweritem/largecontentimage.md), or both.

This property defaults to an appropriate value for UIKit classes, otherwise `nil`.

## See Also

- [var largeContentImage: UIImage?](uilargecontentvieweritem/largecontentimage.md)
  An image that represents an item to display in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](uilargecontentvieweritem/largecontentimageinsets.md)
  Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.
- [var scalesLargeContentImage: Bool](uilargecontentvieweritem/scaleslargecontentimage.md)
  A Boolean value that indicates whether the view scales the item’s image to a larger size or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentvieweritem/largecontenttitle)*