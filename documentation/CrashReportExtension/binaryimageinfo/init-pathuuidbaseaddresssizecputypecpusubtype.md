# init(path:uuid:baseAddress:size:cpuType:cpuSubType:)

**Framework**: CrashReportExtension  
**Kind**: init

Creates a binary image info instance.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(path: String, uuid: UUID?, baseAddress: UInt64, size: UInt64, cpuType: cpu_type_t, cpuSubType: cpu_subtype_t)
```

## Parameters

- `path`: The path to the binary image.
- `uuid`: The UUID of the binary image.
- `baseAddress`: The base address of the binary image.
- `size`: The size of the binary image.
- `cpuType`: The binary image’s CPU type.
- `cpuSubType`: The binary image’s CPU subtype.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/binaryimageinfo/init(path:uuid:baseaddress:size:cputype:cpusubtype:))*