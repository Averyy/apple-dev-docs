# SCScreenshotConfiguration.DisplayIntent

**Framework**: ScreenCaptureKit  
**Kind**: enum

A value that specifies the type of display a screenshot rendering optimizes for.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum DisplayIntent
```

#### Overview

Specifying local or canonical display attributes optimizes output for presentation on either the capture display or any high dynamic range display.

## Topics

### Enumeration Cases
- [SCScreenshotConfiguration.DisplayIntent.canonical](scscreenshotconfiguration/displayintent-swift.enum/canonical.md)
  Specifies that the screenshot renders with canonical display attributes optimizing output for presentation on a high dynamic range display.
- [SCScreenshotConfiguration.DisplayIntent.local](scscreenshotconfiguration/displayintent-swift.enum/local.md)
  Specifies that the screenshot renders with local display attributes optimizing output for presentation on the capture display.
### Initializers
- [init?(rawValue: Int)](scscreenshotconfiguration/displayintent-swift.enum/init(rawvalue:).md)
  Creates a display intent object from the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/displayintent-swift.enum)*