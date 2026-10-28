# SCScreenshotConfiguration.DisplayIntent

**Framework**: ScreenCaptureKit  
**Kind**: enum  
**Role**: Enumeration

A value that specifies the type of display a screenshot rendering optimizes for.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
enum DisplayIntent
```

```c
enum SCScreenshotDisplayIntent : NSInteger;
```

## Overview

Specifying local or canonical display attributes optimizes output for presentation on either the capture display or any high dynamic range display.

## Topics

### Enumeration Cases
- [SCScreenshotConfiguration.DisplayIntent.canonical](./displayintent-swift.enum/canonical.md)
  Specifies that the screenshot renders with canonical display attributes optimizing output for presentation on a high dynamic range display.
- [SCScreenshotConfiguration.DisplayIntent.local](./displayintent-swift.enum/local.md)
  Specifies that the screenshot renders with local display attributes optimizing output for presentation on the capture display.
### Initializers
- [init?(rawValue: Int)](./displayintent-swift.enum/init%28rawvalue%29.md)
  Creates a display intent object from the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scscreenshotconfiguration/displayintent-swift.enum)*