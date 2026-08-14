# BinaryImageInfo

**Framework**: CrashReportExtension  
**Kind**: struct

A type that represents a binary image loaded in the crashed process.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BinaryImageInfo
```

## Topics

### Creating an instance
- [init(path: String, uuid: UUID?, baseAddress: UInt64, size: UInt64, cpuType: cpu_type_t, cpuSubType: cpu_subtype_t)](binaryimageinfo/init(path:uuid:baseaddress:size:cputype:cpusubtype:).md)
  Creates a binary image info instance.
### Inspecting binary image properties
- [let baseAddress: UInt64](binaryimageinfo/baseaddress.md)
  The base address of the binary image.
- [let cpuSubType: cpu_subtype_t](binaryimageinfo/cpusubtype.md)
  The binary image’s CPU subtype.
- [let cpuType: cpu_type_t](binaryimageinfo/cputype.md)
  The binary image’s CPU type.
- [let path: String](binaryimageinfo/path.md)
  The path to the binary image.
- [let size: UInt64](binaryimageinfo/size.md)
  The size of the binary image.
- [let uuid: UUID?](binaryimageinfo/uuid.md)
  The UUID of the binary image.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var reason: CrashReason](crashedprocess/reason.md)
  Contextual information about the reported crash.
- [struct CrashReason](crashreason.md)
  Context information about the crash being reported
- [var binaryImages: [BinaryImageInfo]](crashedprocess/binaryimages.md)
  A list of binary images from the crashed process.
- [var corpsePort: mach_port_t](crashedprocess/corpseport.md)
  A property that provides a Mach port to the crashed process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/binaryimageinfo)*