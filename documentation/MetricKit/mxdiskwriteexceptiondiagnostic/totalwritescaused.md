# totalWritesCaused

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total amount of data written to disk or other long-term storage during the disk write exception.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`totalBytesWritten`](../diskwriteexceptiondiagnostic/totalbyteswritten.md) instead.

## Declaration

```swift
var totalWritesCaused: Measurement<UnitInformationStorage> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitInformationStorage *> * totalWritesCaused;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiskwriteexceptiondiagnostic/totalwritescaused)*