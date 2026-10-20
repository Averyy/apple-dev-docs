# directionalLayoutMargins

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The margins between the content and the edges of the content view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var directionalLayoutMargins: NSDirectionalEdgeInsets { get set }
```

#### Discussion

When you preserve superview layout margins on one or both axes, this value specifies the minimum margins. The inherited margins may be larger.

By default, the content view preserves the layout margins of its superview on both axes. You can customize this behavior by changing [`axesPreservingSuperviewLayoutMargins`](./axespreservingsuperviewlayoutmargins.md).

## See Also

### Customizing layout
- [var axesPreservingSuperviewLayoutMargins: UIAxis](./axespreservingsuperviewlayoutmargins.md)
  A Boolean value that determines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.
- [var prefersSideBySideTextAndSecondaryText: Bool](./preferssidebysidetextandsecondarytext.md)
  A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [var imageToTextPadding: CGFloat](./imagetotextpadding.md)
  The padding between the image and text.
- [var textToSecondaryTextHorizontalPadding: CGFloat](./texttosecondarytexthorizontalpadding.md)
  The minimum horizontal padding between the text and secondary text.
- [var textToSecondaryTextVerticalPadding: CGFloat](./texttosecondarytextverticalpadding.md)
  The vertical padding between the text and secondary text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/directionallayoutmargins)*