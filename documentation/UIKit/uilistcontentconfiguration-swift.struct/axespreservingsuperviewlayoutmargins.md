# axesPreservingSuperviewLayoutMargins

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var axesPreservingSuperviewLayoutMargins: UIAxis { get set }
```

## Discussion

By default, the content view preserves the layout margins of its superview on [`both`](../uiaxis/both.md) axes.

## See Also

### Customizing layout
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](./directionallayoutmargins.md)
  The margins between the content and the edges of the content view.
- [var prefersSideBySideTextAndSecondaryText: Bool](./preferssidebysidetextandsecondarytext.md)
  A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [var imageToTextPadding: CGFloat](./imagetotextpadding.md)
  The padding between the image and text.
- [var textToSecondaryTextHorizontalPadding: CGFloat](./texttosecondarytexthorizontalpadding.md)
  The minimum horizontal padding between the text and secondary text.
- [var textToSecondaryTextVerticalPadding: CGFloat](./texttosecondarytextverticalpadding.md)
  The vertical padding between the text and secondary text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/axespreservingsuperviewlayoutmargins)*