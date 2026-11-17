# thumbnail

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The thumbnail image to display in the header.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var thumbnail: CPThumbnailImage { get set }
```

```objc
@property (nonatomic, strong) CPThumbnailImage * thumbnail;
```

## Discussion

The image in this property represents the primary visual content of the header. You can augment the thumbnail image to include overlays or playback progress indicators. For example, you can place sports scores on top the image using a sports overlay.

## See Also

### Managing the header’s content
- [var title: String?](./title.md)
  The primary text to display in the header.
- [var subtitle: String?](./subtitle.md)
  The text to display in the header below the title.
- [var bodyVariants: [NSAttributedString]](./bodyvariants.md)
  An optional array of localized strings to display beneath the subtitle.
- [var actionButtons: [CPButton]](./actionbuttons.md)
  An array of action buttons to display in the header.
- [var wantsAdaptiveBackgroundStyle: Bool](./wantsadaptivebackgroundstyle.md)
  A Boolean value that indicates whether to apply a custom background style to the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/thumbnail)*