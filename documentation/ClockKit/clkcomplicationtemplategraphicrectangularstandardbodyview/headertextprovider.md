# headerTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text provider for the header text.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@_NilHidden
<CLKTextProvider> @objc final var headerTextProvider: CLKTextProvider { get set }
```

## Discussion

The template supports multicolored text from this text provider.

## See Also

### Accessing the Content
- [var headerLabel: Label](./headerlabel.md)
  The SwiftUI view displayed by the template.
- [var body1TextProvider: CLKTextProvider](./body1textprovider.md)
  The text provider for the first row of body text.
- [var body2TextProvider: CLKTextProvider?](./body2textprovider.md)
  The text provider for the second row of body text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangularstandardbodyview/headertextprovider)*