# bodyTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The main body text to display in the complication.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@_NilHidden
<CLKTextProvider> @objc final var bodyTextProvider: CLKTextProvider { get set }
```

#### Discussion

This property supports multicolor text.

## See Also

### Accessing the Content
- [var headerLabel: Label](./headerlabel.md)
  The SwiftUI view displayed by the template.
- [var headerTextProvider: CLKTextProvider](./headertextprovider.md)
  The header text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgaugeview/bodytextprovider)*