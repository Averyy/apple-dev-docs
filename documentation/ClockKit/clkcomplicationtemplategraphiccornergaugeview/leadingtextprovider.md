# leadingTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text provider for the gauge’s leading text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@_NilHidden
<CLKTextProvider?> @objc final var leadingTextProvider: CLKTextProvider? { get set }
```

#### Discussion

The template supports multicolored text from this text provider.

## See Also

### Accessing the Content
- [var label: Label](./label.md)
  The SwiftUI view displayed by the template.
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.
- [var trailingTextProvider: CLKTextProvider?](./trailingtextprovider.md)
  The text provider for the gauge’s trailing text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeview/leadingtextprovider)*