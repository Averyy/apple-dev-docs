# CrashReason

**Framework**: CrashReportExtension  
**Kind**: struct

Context information about the crash being reported

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CrashReason
```

## Topics

### Creating a crash reason
- [init(exception: Int32, codes: [UInt64])](crashreason/init(exception:codes:).md)
  Creates a crash reason instance with the given parameters.
### Inpecting crash reason properties
- [let codes: [UInt64]](crashreason/codes.md)
  An array of exception-specific codes providing additional details.
- [let exception: Int32](crashreason/exception.md)
  The Mach exception type.

## See Also

- [var reason: CrashReason](crashedprocess/reason.md)
  Contextual information about the reported crash.
- [var binaryImages: [BinaryImageInfo]](crashedprocess/binaryimages.md)
  A list of binary images from the crashed process.
- [struct BinaryImageInfo](binaryimageinfo.md)
  A type that represents a binary image loaded in the crashed process.
- [var corpsePort: mach_port_t](crashedprocess/corpseport.md)
  A property that provides a Mach port to the crashed process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/crashreason)*