# line1TextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text to display on the top line of the complication.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var line1TextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * line1TextProvider;
```

## Discussion

Space for text is limited in this particular template so keep strings as short as possible.

When the [`highlightLine2`](./highlightline2.md) property is [`false`](../../Swift/false.md), a tint color is applied to this text. In multicolor environments, the text provider or template provides the tint color. In monochrome environments, the clock face provides the tint color.

## See Also

### Setting the Complication Data
- [var highlightLine2: Bool](./highlightline2.md)
  A Boolean value indicating which line should be drawn with a highlight.
- [var line2TextProvider: CLKTextProvider](./line2textprovider.md)
  The text to display on the bottom line of the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestacktext/line1textprovider)*