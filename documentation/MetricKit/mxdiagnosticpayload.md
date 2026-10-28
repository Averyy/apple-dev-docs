# MXDiagnosticPayload

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

An object that encapsulates a diagnostic report.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticReport`](./diagnosticreport.md), and read the [`DiagnosticResult.crash(_:)`](./diagnosticresult/crash%28_%29.md), [`DiagnosticResult.hang(_:)`](./diagnosticresult/hang%28_%29.md), [`DiagnosticResult.cpuException(_:)`](./diagnosticresult/cpuexception%28_%29.md), [`DiagnosticResult.diskWriteException(_:)`](./diagnosticresult/diskwriteexception%28_%29.md), or [`DiagnosticResult.appLaunch(_:)`](./diagnosticresult/applaunch%28_%29.md) cases instead.

## Declaration

```swift
class MXDiagnosticPayload
```

```objc
@interface MXDiagnosticPayload : NSObject
```

## Overview

The system delivers a diagnostic report as soon as it’s available.

## Topics

### Reading performance metrics
- [var crashDiagnostics: [MXCrashDiagnostic]?](./mxdiagnosticpayload/crashdiagnostics.md)
  The diagnostic reports for app crashes during the reporting period.
- [var cpuExceptionDiagnostics: [MXCPUExceptionDiagnostic]?](./mxdiagnosticpayload/cpuexceptiondiagnostics.md)
  The diagnostic reports for fatal and nonfatal CPU exceptions for the app during the reporting period.
### Reading responsiveness metrics
- [var appLaunchDiagnostics: [MXAppLaunchDiagnostic]?](./mxdiagnosticpayload/applaunchdiagnostics.md)
  The diagnostic reports for the app launch time.
- [var hangDiagnostics: [MXHangDiagnostic]?](./mxdiagnosticpayload/hangdiagnostics.md)
  The diagnostic reports for times when the app was too busy to handle input responsively during the reporting period.
### Reading disk access metrics
- [var diskWriteExceptionDiagnostics: [MXDiskWriteExceptionDiagnostic]?](./mxdiagnosticpayload/diskwriteexceptiondiagnostics.md)
  The diagnostic reports for disk write exceptions for the app during the reporting period.
### Generating a report
- [func jsonRepresentation() -> Data](./mxdiagnosticpayload/jsonrepresentation%28%29.md)
  Returns the contents of the payload in JSON format.
- [func dictionaryRepresentation() -> [AnyHashable : Any]](./mxdiagnosticpayload/dictionaryrepresentation%28%29.md)
  Returns the results of the payload as a dictionary.
### Reading information about the payload
- [var timeStampBegin: Date](./mxdiagnosticpayload/timestampbegin.md)
  The starting time of the reporting period.
- [var timeStampEnd: Date](./mxdiagnosticpayload/timestampend.md)
  The ending time of the reporting period.
### Initializers
- [init?(coder: NSCoder)](./mxdiagnosticpayload/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Metric and diagnostic reports
- [class MXMetricManager](./mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [class MXMetricPayload](./mxmetricpayload.md)
  An object that encapsulates a daily metrics report.
- [protocol MXMetricManagerSubscriber](./mxmetricmanagersubscriber.md)
  A protocol defining a method for receiving a daily metrics report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload)*