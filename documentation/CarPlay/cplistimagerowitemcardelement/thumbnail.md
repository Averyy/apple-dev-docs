# thumbnail

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The thumbnail object that provides the image content.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var thumbnail: CPThumbnailImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) CPThumbnailImage * thumbnail;
```

## Discussion

If you initialized the element with a thumbnail image, use this property to update the thumbnail image for your type. For example, you might assign a new thumbnail with updated overlay content. If you didn’t initialize your type with a thumbnail object, the value in this property is `nil` initially.

## See Also

### Getting the image behavior
- [var showsImageFullHeight: Bool](./showsimagefullheight.md)
  A Boolean value that indicates whether to use a full-height image for the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/thumbnail)*