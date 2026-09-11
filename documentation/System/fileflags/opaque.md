# opaque

**Framework**: System  
**Kind**: property

Directory is opaque when viewed through a union mount.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static var opaque: FileFlags { get }
```

#### Discussion

The corresponding C constant is `UF_OPAQUE`.

> **Note**: This flag may be changed by the file owner or superuser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags/opaque)*