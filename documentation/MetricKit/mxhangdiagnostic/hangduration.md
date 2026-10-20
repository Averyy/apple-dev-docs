# hangDuration

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The amount of time the app is busy and unable to respond to user interaction.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`hangDuration`](../hangdiagnostic/hangduration.md) instead.

## Declaration

```swift
var hangDuration: Measurement<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitDuration *> * hangDuration;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxhangdiagnostic/hangduration)*