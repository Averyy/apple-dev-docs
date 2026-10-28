# textStyle

**Framework**: TVMLKit  
**Kind**: property  
**Role**: Instance Property

The style applied to the text in an element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
var textStyle: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * textStyle;
```

## Discussion

For possible values, see [Text Style Values](../text-style-values.md).

## See Also

### Changing the Text of an Element
- [var fontSize: CGFloat](./fontsize.md)
  The font size applied to any text contained in the element.
- [var fontWeight: String?](./fontweight.md)
  A string indicating how thick or thin the font is.
- [var maxTextLines: Int](./maxtextlines.md)
  The maximum number of lines of text allowed inside of the element.
- [var textAlignment: NSTextAlignment](./textalignment.md)
  The horizontal alignment of text within an element.
- [var textHighlightStyle: String?](./texthighlightstyle.md)
  A string indicating how a label reacts when it is in focus.
- [var textMinimumScaleFactor: CGFloat](./textminimumscalefactor.md)
  The minimum size text can be if the original text size does not fit in an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelementstyle/textstyle)*