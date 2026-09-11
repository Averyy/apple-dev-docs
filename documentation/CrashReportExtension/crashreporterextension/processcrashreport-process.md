# processCrashReport(process:)

**Framework**: CrashReportExtension  
**Kind**: method  
**Required**: Yes

A method the system calls when a crash report is ready to be processed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- visionOS ?+

## Declaration

```swift
func processCrashReport(process: CrashedProcess)
```

#### Discussion

Implement this method by inspecting the [`CrashedProcess`](crashedprocess.md) object to prepare a crash report. You can then persist this report or send it back to your own server.

## Parameters

- `process`: Client for accessing crash data (corpse port, symbolication, etc.)

## See Also

- [class CrashedProcess](crashedprocess.md)
  A synchronous client for accessing crash data from the host process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashreporterextension/processcrashreport(process:))*