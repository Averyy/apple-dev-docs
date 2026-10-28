# MXUnitSignalBars

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

A unit of measure for the number of bars of cellular network connectivity.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`SignalBars`](./signalbars.md) instead.

## Declaration

```swift
class MXUnitSignalBars
```

```objc
@interface MXUnitSignalBars : NSDimension
```

## Overview

Cellular connectivity measures the relative strength of the device’s signal reception in decibels, which usually falls in a range of 0 to -110.

`MXUnitSignalBars` defines the base unit as bars corresponding to the bars in the cellular connection status icon at the top of a device screen.

## Topics

### Measuring Connection Strength
- [class var bars: MXUnitSignalBars](./mxunitsignalbars/bars.md)
  The number of bars of connectivity to the cellular network.

## Relationships

### Inherits From
- [Dimension](../Foundation/dimension.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [class MXCallStackTree](./mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](./mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](./mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](./mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXHistogramBucket](./mxhistogrambucket.md)
  An object representing a bucket of data in a histogram.
- [class MXDiagnostic](./mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](./mxmetric.md)
  An abstract data class for a metric.
- [struct MXError](./mxerror.md)
  Error domain for error handling of app metrics.
- [MXError.Code](./mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](./mxerrordomain.md)
  Error domain for error values from app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](./mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](./mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.
- [class MXUnitAveragePixelLuminance](./mxunitaveragepixelluminance.md)
  A unit of measure of pixel luminosity on an OLED display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxunitsignalbars)*