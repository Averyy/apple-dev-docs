# reason

**Framework**: CrashReportExtension  
**Kind**: property

Contextual information about the reported crash.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
final var reason: CrashReason
```

## See Also

- [struct CrashReason](crashreason.md)
  Context information about the crash being reported
- [var binaryImages: [BinaryImageInfo]](crashedprocess/binaryimages.md)
  A list of binary images from the crashed process.
- [struct BinaryImageInfo](binaryimageinfo.md)
  A type that represents a binary image loaded in the crashed process.
- [var corpsePort: mach_port_t](crashedprocess/corpseport.md)
  A property that provides a Mach port to the crashed process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashedprocess/reason)*