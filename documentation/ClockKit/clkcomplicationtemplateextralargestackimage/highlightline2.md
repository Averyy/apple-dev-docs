# highlightLine2

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating which line should be drawn with a highlight.

**Availability**:
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var highlightLine2: Bool { get set }
```

```objc
@property (nonatomic) BOOL highlightLine2;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the text in row two is rendered with a highlight. When the value is [`false`](../../Swift/false.md), the image on line one is rendered with a highlight. The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Setting the Complication Data
- [var line1ImageProvider: CLKImageProvider](./line1imageprovider.md)
  The image to display on the top line of the complication.
- [var line2TextProvider: CLKTextProvider](./line2textprovider.md)
  The text to display on the bottom line of the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateextralargestackimage/highlightline2)*