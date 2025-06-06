# allowsDefaultTighteningForTruncation

**Framework**: AppKit  
**Kind**: property

A Boolean value that controls whether single-line text fields tighten intercharacter spacing before truncating the text.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var allowsDefaultTighteningForTruncation: Bool { get set }
```

#### Discussion

The text field ignores this property when its value is an attributed string.

## See Also

- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](nstextfield/linebreakstrategy.md)
  The strategy that the system uses to break lines when laying out multiple lines of text.
- [var maximumNumberOfLines: Int](nstextfield/maximumnumberoflines.md)
  The maximum number of lines a wrapping text field displays before clipping or truncating the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/allowsdefaulttighteningfortruncation)*