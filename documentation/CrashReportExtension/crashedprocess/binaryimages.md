# binaryImages

**Framework**: CrashReportExtension  
**Kind**: property  
**Role**: Instance Property

A list of binary images from the crashed process.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS
- visionOS
- watchOS

## Declaration

```swift
final var binaryImages: [BinaryImageInfo] { get }
```

## See Also

### Accessing process properties
- [var reason: CrashReason](./reason.md)
  Contextual information about the reported crash.
- [struct CrashReason](../crashreason.md)
  Context information about the crash being reported
- [struct BinaryImageInfo](../binaryimageinfo.md)
  A type that represents a binary image loaded in the crashed process.
- [var corpsePort: mach_port_t](./corpseport.md)
  A property that provides a Mach port to the crashed process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashedprocess/binaryimages)*