# MXUnitAveragePixelLuminance

**Framework**: MetricKit  
**Kind**: class

A unit of measure of pixel luminosity on an OLED display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class MXUnitAveragePixelLuminance
```

#### Overview

Luminosity represents the brightness of each red, green, and blue component pixel. Unlike LCD displays, each pixel requires power to display a color, and white draws the most power per pixel.

`MXUnitAveragePixelLuminance` defines the base unit as the average luminance of all the pixels on the screen for some period of time. Reducing the average luminance of the display reduces the amount of power consumed by the app.

## Topics

### Measuring Average Pixel Luminance
- [class var apl: MXUnitAveragePixelLuminance](mxunitaveragepixelluminance/apl.md)
  The average number of powered pixels on a OLED display.

## Relationships

### Inherits From
- [Dimension](../foundation/dimension.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class MXCallStackTree](mxcallstacktree.md)
  An object representing the call stack for an exception.
- [class MXMetaData](mxmetadata.md)
  An object containing system-level information about the device.
- [class MXAverage](mxaverage.md)
  A unit of measure for an average.
- [class MXHistogram](mxhistogram.md)
  An object representing a histogram of data values of the same type of unit.
- [class MXHistogramBucket](mxhistogrambucket.md)
  An object representing a bucket of data in a histogram.
- [class MXDiagnostic](mxdiagnostic.md)
  An abstract data class for a diagnostic.
- [class MXMetric](mxmetric.md)
  An abstract data class for a metric.
- [struct MXError](mxerror.md)
  Error domain for error handling of app metrics.
- [MXError.Code](mxerror/code.md)
  Error codes for error values from app metrics.
- [let MXErrorDomain: String](mxerrordomain.md)
  Error domain for error values from app metrics.
- [class MXCrashDiagnosticObjectiveCExceptionReason](mxcrashdiagnosticobjectivecexceptionreason.md)
  An object that represents the exception reason for an uncaught ObjC exception.
- [class MXSignpostRecord](mxsignpostrecord.md)
  An object representing the record for a signpost interval or event.
- [class MXUnitSignalBars](mxunitsignalbars.md)
  A unit of measure for the number of bars of cellular network connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxunitaveragepixelluminance)*