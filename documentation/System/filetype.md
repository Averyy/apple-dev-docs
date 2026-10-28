# FileType

**Framework**: System  
**Kind**: struct  
**Role**: Structure

A file type matching those contained in a C `mode_t`.

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
struct FileType
```

## Overview

> **Note**: Only available on Unix-like platforms.

## Topics

### Initializers
- [init(rawValue: CInterop.Mode)](./filetype/init%28rawvalue%29.md)
  Creates a strongly-typed file type from the raw C `mode_t`.
### Instance Properties
- [var rawValue: CInterop.Mode](./filetype/rawvalue.md)
  The raw file-type bits from the C mode.
### Type Properties
- [static var blockSpecial: FileType](./filetype/blockspecial.md)
  Block special device
- [static var characterSpecial: FileType](./filetype/characterspecial.md)
  Character special device
- [static var directory: FileType](./filetype/directory.md)
  Directory
- [static var fifo: FileType](./filetype/fifo.md)
  FIFO (or named pipe)
- [static var regular: FileType](./filetype/regular.md)
  Regular file
- [static var socket: FileType](./filetype/socket.md)
  Socket
- [static var symbolicLink: FileType](./filetype/symboliclink.md)
  Symbolic link
- [static var whiteout: FileType](./filetype/whiteout.md)
  Whiteout file

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

*[View on Apple Developer](https://developer.apple.com/documentation/system/filetype)*