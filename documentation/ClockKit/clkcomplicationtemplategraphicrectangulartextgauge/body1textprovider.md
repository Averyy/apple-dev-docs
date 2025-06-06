# body1TextProvider

**Framework**: ClockKit  
**Kind**: property

The main body text to display in the complication.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var body1TextProvider: CLKTextProvider { get set }
```

#### Discussion

In watchOS 5 and earlier, the system always displays the text as white. In watchOS 6 and later, it can display multicolor text.

## See Also

- [var headerTextProvider: CLKTextProvider](clkcomplicationtemplategraphicrectangulartextgauge/headertextprovider.md)
  The header text to display in the complication.
- [var headerImageProvider: CLKFullColorImageProvider?](clkcomplicationtemplategraphicrectangulartextgauge/headerimageprovider.md)
  The header image to display.
- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphicrectangulartextgauge/gaugeprovider.md)
  The gauge to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgauge/body1textprovider)*