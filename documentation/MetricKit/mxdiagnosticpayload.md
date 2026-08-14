# MXDiagnosticPayload

**Framework**: MetricKit  
**Kind**: class

An object that encapsulates a diagnostic report.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class MXDiagnosticPayload
```

#### Overview

The system delivers a diagnostic report as soon as it’s available.

## Topics

### Reading performance metrics
- [var crashDiagnostics: [MXCrashDiagnostic]?](mxdiagnosticpayload/crashdiagnostics.md)
  The diagnostic reports for app crashes during the reporting period.
- [var cpuExceptionDiagnostics: [MXCPUExceptionDiagnostic]?](mxdiagnosticpayload/cpuexceptiondiagnostics.md)
  The diagnostic reports for fatal and nonfatal CPU exceptions for the app during the reporting period.
### Reading responsiveness metrics
- [var appLaunchDiagnostics: [MXAppLaunchDiagnostic]?](mxdiagnosticpayload/applaunchdiagnostics.md)
  The diagnostic reports for the app launch time.
- [var hangDiagnostics: [MXHangDiagnostic]?](mxdiagnosticpayload/hangdiagnostics.md)
  The diagnostic reports for times when the app was too busy to handle input responsively during the reporting period.
### Reading disk access metrics
- [var diskWriteExceptionDiagnostics: [MXDiskWriteExceptionDiagnostic]?](mxdiagnosticpayload/diskwriteexceptiondiagnostics.md)
  The diagnostic reports for disk write exceptions for the app during the reporting period.
### Generating a report
- [func jsonRepresentation() -> Data](mxdiagnosticpayload/jsonrepresentation.md)
  Returns the contents of the payload in JSON format.
- [func dictionaryRepresentation() -> [AnyHashable : Any]](mxdiagnosticpayload/dictionaryrepresentation.md)
  Returns the results of the payload as a dictionary.
### Reading information about the payload
- [var timeStampBegin: Date](mxdiagnosticpayload/timestampbegin.md)
  The starting time of the reporting period.
- [var timeStampEnd: Date](mxdiagnosticpayload/timestampend.md)
  The ending time of the reporting period.
### Initializers
- [init?(coder: NSCoder)](mxdiagnosticpayload/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MXMetricManager](mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [class MXMetricPayload](mxmetricpayload.md)
  An object that encapsulates a daily metrics report.
- [protocol MXMetricManagerSubscriber](mxmetricmanagersubscriber.md)
  A protocol defining a method for receiving a daily metrics report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload)*