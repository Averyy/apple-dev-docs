# bodyVariants

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An optional array of localized strings to display beneath the subtitle.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var bodyVariants: [NSAttributedString] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSAttributedString *> * bodyVariants;
```

## Discussion

Specify strings in the array from most to least preferred. The system chooses the first string that fits the available space and displays it below the subtitle.

## See Also

### Managing the header’s content
- [var thumbnail: CPThumbnailImage](./thumbnail.md)
  The thumbnail image to display in the header.
- [var title: String?](./title.md)
  The primary text to display in the header.
- [var subtitle: String?](./subtitle.md)
  The text to display in the header below the title.
- [var actionButtons: [CPButton]](./actionbuttons.md)
  An array of action buttons to display in the header.
- [var wantsAdaptiveBackgroundStyle: Bool](./wantsadaptivebackgroundstyle.md)
  A Boolean value that indicates whether to apply a custom background style to the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/bodyvariants)*