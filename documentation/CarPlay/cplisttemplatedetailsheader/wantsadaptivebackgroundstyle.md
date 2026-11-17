# wantsAdaptiveBackgroundStyle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to apply a custom background style to the header.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var wantsAdaptiveBackgroundStyle: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=wantsAdaptiveBackgroundStyle) BOOL adaptiveBackgroundStyle;
```

## Discussion

When the value of this property is `true`, the system uses perceptually aware color transformations to create a background from the header’s thumbnail image. The background adapts to the current interface style preferences and adjusts automatically to light and dark interfaces. When the value of this property is `false`, CarPlay displays the standard background. The default value of this property is `false`.

## See Also

### Managing the header’s content
- [var thumbnail: CPThumbnailImage](./thumbnail.md)
  The thumbnail image to display in the header.
- [var title: String?](./title.md)
  The primary text to display in the header.
- [var subtitle: String?](./subtitle.md)
  The text to display in the header below the title.
- [var bodyVariants: [NSAttributedString]](./bodyvariants.md)
  An optional array of localized strings to display beneath the subtitle.
- [var actionButtons: [CPButton]](./actionbuttons.md)
  An array of action buttons to display in the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/wantsadaptivebackgroundstyle)*