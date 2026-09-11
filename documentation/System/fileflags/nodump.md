# noDump

**Framework**: System  
**Kind**: property

Do not dump the file during backups.

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
static var noDump: FileFlags { get }
```

#### Discussion

The corresponding C constant is `UF_NODUMP`.

> **Note**: This flag may be changed by the file owner or superuser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags/nodump)*