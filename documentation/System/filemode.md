# FileMode

**Framework**: System  
**Kind**: struct

A strongly-typed file mode representing a C `mode_t`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
struct FileMode
```

#### Overview

> **Note**: Only available on Unix-like platforms.

## Topics

### Initializers
- [init(rawValue: CInterop.Mode)](filemode/init(rawvalue:).md)
  Creates a strongly-typed `FileMode` from the raw C value.
- [init(type: FileType, permissions: FilePermissions)](filemode/init(type:permissions:).md)
  Creates a `FileMode` from the given file type and permissions.
### Instance Properties
- [var permissions: FilePermissions](filemode/permissions.md)
  The file’s permissions, from the mode’s permission bits.
- [var rawValue: CInterop.Mode](filemode/rawvalue.md)
  The raw C mode.
- [var type: FileType](filemode/type.md)
  The file’s type, from the mode’s file-type bits.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filemode)*