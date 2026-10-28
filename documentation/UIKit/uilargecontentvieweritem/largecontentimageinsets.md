# largeContentImageInsets

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Insets to adjust the position of the item’s image so it appears visually centered in the large content viewer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var largeContentImageInsets: UIEdgeInsets { get }
```

```objc
@property (nonatomic, assign, readonly) UIEdgeInsets largeContentImageInsets;
```

## Discussion

This property defaults to [`zero`](../uiedgeinsets/zero.md).

## See Also

### Configuring display properties
- [var largeContentTitle: String?](./largecontenttitle.md)
  A string that describes an item to display in the large content viewer.
- [var largeContentImage: UIImage?](./largecontentimage.md)
  An image that represents an item to display in the large content viewer.
- [var scalesLargeContentImage: Bool](./scaleslargecontentimage.md)
  A Boolean value that indicates whether the view scales the item’s image to a larger size or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentvieweritem/largecontentimageinsets)*