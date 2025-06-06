# init(gaugeProvider:bottomImageProvider:centerTextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template that has an open circular gauge, a small image at the bottom, and a small amount of text in the center.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, bottomImageProvider: CLKFullColorImageProvider, centerTextProvider: CLKTextProvider)
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `bottomImageProvider`: The image provider for a small image at the bottom of the template. This template uses a full-color image.
- `centerTextProvider`: The text provider for the center text. The template supports multicolored text from this text provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularopengaugeimage/init(gaugeprovider:bottomimageprovider:centertextprovider:))*