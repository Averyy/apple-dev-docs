# FileMode

**Framework**: System  
**Kind**: struct  
**Role**: Structure

A strongly-typed file mode representing a C `mode_t`.

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
@frozen
struct FileMode
```

## Overview

> **Note**: Only available on Unix-like platforms.

## Topics

### Initializers
- [init(rawValue: CInterop.Mode)](./filemode/init%28rawvalue%29.md)
  Creates a strongly-typed `FileMode` from the raw C value.
- [init(type: FileType, permissions: FilePermissions)](./filemode/init%28type,permissions%29.md)
  Creates a `FileMode` from the given file type and permissions.
### Instance Properties
- [var permissions: FilePermissions](./filemode/permissions.md)
  The file’s permissions, from the mode’s permission bits.
- [var rawValue: CInterop.Mode](./filemode/rawvalue.md)
  The raw C mode.
- [var type: FileType](./filemode/type.md)
  The file’s type, from the mode’s file-type bits.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filemode)*