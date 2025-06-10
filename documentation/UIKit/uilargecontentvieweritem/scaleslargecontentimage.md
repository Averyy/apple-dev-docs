# scalesLargeContentImage

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the view scales the item’s image to a larger size or not.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var scalesLargeContentImage: Bool { get }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/swift/false), the viewer displays the image at its intrinsic size.

> 💡 **Tip**:  For best results when scaling, use a PDF asset with the Preserve Vector Data checked in the asset catalog.

## See Also

- [var largeContentTitle: String?](uilargecontentvieweritem/largecontenttitle.md)
  A string that describes an item to display in the large content viewer.
- [var largeContentImage: UIImage?](uilargecontentvieweritem/largecontentimage.md)
  An image that represents an item to display in the large content viewer.
- [var largeContentImageInsets: UIEdgeInsets](uilargecontentvieweritem/largecontentimageinsets.md)
  Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentvieweritem/scaleslargecontentimage)*