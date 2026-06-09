# corpsePort

**Framework**: CrashReportExtension  
**Kind**: property

A property that provides a Mach port to the crashed process.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
final var corpsePort: mach_port_t { get }
```

#### Discussion

The corpse port is a read-only task port for a process that terminated but is still available for inspecting state and data. Send Mach IPC interface commands over this port to find leaks, symbolicate backtraces, and more. For example, call `task_threads` to enumerate threads, and call `mach_vm_read` to read memory from the process.

## See Also

- [var reason: CrashReason](crashedprocess/reason.md)
  Contextual information about the reported crash.
- [struct CrashReason](crashreason.md)
  Context information about the crash being reported
- [var binaryImages: [BinaryImageInfo]](crashedprocess/binaryimages.md)
  A list of binary images from the crashed process.
- [struct BinaryImageInfo](binaryimageinfo.md)
  A type that represents a binary image loaded in the crashed process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashedprocess/corpseport)*