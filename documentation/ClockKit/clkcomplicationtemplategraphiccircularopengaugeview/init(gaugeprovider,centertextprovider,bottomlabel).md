# init(gaugeProvider:centerTextProvider:bottomLabel:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template that has an open circular gauge, a small amount of text in the center, and a small SwiftUI view at the bottom.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, centerTextProvider: CLKTextProvider, bottomLabel: Label)
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `centerTextProvider`: The text provider for the center text. The template supports multicolored text from this text provider.
- `bottomLabel`: The SwiftUI view displayed by the template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularopengaugeview/init(gaugeprovider:centertextprovider:bottomlabel:))*