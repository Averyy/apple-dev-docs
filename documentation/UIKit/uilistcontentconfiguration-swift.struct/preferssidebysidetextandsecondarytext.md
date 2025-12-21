# prefersSideBySideTextAndSecondaryText

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the configuration positions the text and secondary text side by side.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var prefersSideBySideTextAndSecondaryText: Bool { get set }
```

#### Discussion

When this value is [`true`](https://developer.apple.com/documentation/Swift/true), the configuration positions the text and secondary text side by side if there’s sufficient space. Otherwise, the configuration stacks the text in a vertical layout.

## See Also

- [var axesPreservingSuperviewLayoutMargins: UIAxis](uilistcontentconfiguration-swift.struct/axespreservingsuperviewlayoutmargins.md)
  A Boolean value that determines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](uilistcontentconfiguration-swift.struct/directionallayoutmargins.md)
  The margins between the content and the edges of the content view.
- [var imageToTextPadding: CGFloat](uilistcontentconfiguration-swift.struct/imagetotextpadding.md)
  The padding between the image and text.
- [var textToSecondaryTextHorizontalPadding: CGFloat](uilistcontentconfiguration-swift.struct/texttosecondarytexthorizontalpadding.md)
  The minimum horizontal padding between the text and secondary text.
- [var textToSecondaryTextVerticalPadding: CGFloat](uilistcontentconfiguration-swift.struct/texttosecondarytextverticalpadding.md)
  The vertical padding between the text and secondary text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/preferssidebysidetextandsecondarytext)*