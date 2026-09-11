# userAppend

**Framework**: System  
**Kind**: property

Writes to the file may only append.

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
static var userAppend: FileFlags { get }
```

#### Discussion

The corresponding C constant is `UF_APPEND`.

> **Note**: This flag may be changed by the file owner or superuser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags/userappend)*