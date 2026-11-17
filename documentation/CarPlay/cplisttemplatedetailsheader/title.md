# title

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The primary text to display in the header.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * title;
```

## Discussion

Use this property to specify song titles, show names, or primary content descriptions. The text from this property appears prominently below or alongside the thumbnail image in the header area.

## See Also

### Managing the header’s content
- [var thumbnail: CPThumbnailImage](./thumbnail.md)
  The thumbnail image to display in the header.
- [var subtitle: String?](./subtitle.md)
  The text to display in the header below the title.
- [var bodyVariants: [NSAttributedString]](./bodyvariants.md)
  An optional array of localized strings to display beneath the subtitle.
- [var actionButtons: [CPButton]](./actionbuttons.md)
  An array of action buttons to display in the header.
- [var wantsAdaptiveBackgroundStyle: Bool](./wantsadaptivebackgroundstyle.md)
  A Boolean value that indicates whether to apply a custom background style to the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/title)*