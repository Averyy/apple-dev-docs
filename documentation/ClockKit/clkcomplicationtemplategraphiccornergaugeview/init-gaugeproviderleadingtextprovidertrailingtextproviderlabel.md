# init(gaugeProvider:leadingTextProvider:trailingTextProvider:label:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template with the provided gauge and view.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider? = nil, trailingTextProvider: CLKTextProvider? = nil, label: Label)
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `leadingTextProvider`: The text provider for the gauge’s leading text. The template supports multicolored text from this text provider.
- `trailingTextProvider`: The text provider for the gauge’s trailing text. The template supports multicolored text from this text provider.
- `label`: The SwiftUI view displayed by the template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeview/init(gaugeprovider:leadingtextprovider:trailingtextprovider:label:))*