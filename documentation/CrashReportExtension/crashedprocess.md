# CrashedProcess

**Framework**: CrashReportExtension  
**Kind**: class

A synchronous client for accessing crash data from the host process.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
final class CrashedProcess
```

#### Overview

Your extension receives this type as the parameter to [`processCrashReport(process:)`](crashreporterextension/processcrashreport(process:).md). Use this class to access symbolication and binary images, and perform symbol lookup. You can also access the [`corpsePort`](crashedprocess/corpseport.md) to send Mach IPC commands to the crashed process.

## Topics

### Accessing process properties
- [var reason: CrashReason](crashedprocess/reason.md)
  Contextual information about the reported crash.
- [struct CrashReason](crashreason.md)
  Context information about the crash being reported
- [var binaryImages: [BinaryImageInfo]](crashedprocess/binaryimages.md)
  A list of binary images from the crashed process.
- [struct BinaryImageInfo](binaryimageinfo.md)
  A type that represents a binary image loaded in the crashed process.
- [var corpsePort: mach_port_t](crashedprocess/corpseport.md)
  A property that provides a Mach port to the crashed process.
### Symbolicating addresses
- [func symbolicateAddress(UInt64) -> [SymbolicatedFrame]](crashedprocess/symbolicateaddress(_:).md)
  Symbolicates an address, returning symbol info with inline frame expansion.
- [func symbolicateAddresses([UInt64]) -> [[SymbolicatedFrame]]](crashedprocess/symbolicateaddresses(_:).md)
  Symbolicates an array of addresses, returning symbol information with inline frame expansion.
- [struct SymbolicatedFrame](symbolicatedframe.md)
  A type that represents a single symbolicated stack frame.
### Accessing symbols
- [func symbolAddress(imageName: String?, symbolName: String) -> UInt64](crashedprocess/symboladdress(imagename:symbolname:).md)
  Looks up a symbol’s address by name.

## See Also

- [func processCrashReport(process: CrashedProcess)](crashreporterextension/processcrashreport(process:).md)
  A method the system calls when a crash report is ready to be processed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashedprocess)*