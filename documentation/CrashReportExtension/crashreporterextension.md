# CrashReporterExtension

**Framework**: CrashReportExtension  
**Kind**: protocol

The base type for crash reporter extensions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS ?+

## Declaration

```swift
protocol CrashReporterExtension : AppExtension
```

#### Overview

Conform to this protocol and implement [`processCrashReport(process:)`](crashreporterextension/processcrashreport(process:).md) to create a crash reporter. Your extension runs in its own process, separate from the crashed app.

The following example shows an implementation that accesses the crashed process’s [`corpsePort`](crashedprocess/corpseport.md) and [`binaryImages`](crashedprocess/binaryimages.md) for use in generating a crash report.

```swift
@main
struct MyCrashExtension: CrashReporterExtension {
    func processCrashReport(process: CrashedProcess) {
        let corpsePort = process.corpsePort
        let images = process.binaryImages
        // Generate your crash report...
    }
}
```

After collecting the needed information from the crashed process, you can persist your crash report or send it back to a server you control.

## Topics

### Processing a crash report
- [func processCrashReport(process: CrashedProcess)](crashreporterextension/processcrashreport(process:).md)
  A method the system calls when a crash report is ready to be processed.
- [class CrashedProcess](crashedprocess.md)
  A synchronous client for accessing crash data from the host process.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashreporterextension)*