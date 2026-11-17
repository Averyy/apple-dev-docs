# subtitle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The text to display in the header below the title.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var subtitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * subtitle;
```

## Discussion

Use this property to specify additional metadata or contextual information about the content. For example, you might specify the name of an artist or a description of an episode. The text from this property appears below the title, and it displays with reduced visual prominence.

## See Also

### Managing the header’s content
- [var thumbnail: CPThumbnailImage](./thumbnail.md)
  The thumbnail image to display in the header.
- [var title: String?](./title.md)
  The primary text to display in the header.
- [var bodyVariants: [NSAttributedString]](./bodyvariants.md)
  An optional array of localized strings to display beneath the subtitle.
- [var actionButtons: [CPButton]](./actionbuttons.md)
  An array of action buttons to display in the header.
- [var wantsAdaptiveBackgroundStyle: Bool](./wantsadaptivebackgroundstyle.md)
  A Boolean value that indicates whether to apply a custom background style to the header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/subtitle)*