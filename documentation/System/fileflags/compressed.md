# compressed

**Framework**: System  
**Kind**: property

File is compressed at the file system level.

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
static var compressed: FileFlags { get }
```

#### Discussion

The corresponding C constant is `UF_COMPRESSED`.

> **Note**: This flag is read-only. Attempting to change it will result in undefined behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/fileflags/compressed)*