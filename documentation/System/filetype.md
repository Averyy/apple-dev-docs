# FileType

**Framework**: System  
**Kind**: struct

A file type matching those contained in a C `mode_t`.

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
struct FileType
```

#### Overview

> **Note**: Only available on Unix-like platforms.

## Topics

### Initializers
- [init(rawValue: CInterop.Mode)](filetype/init(rawvalue:).md)
  Creates a strongly-typed file type from the raw C `mode_t`.
### Instance Properties
- [var rawValue: CInterop.Mode](filetype/rawvalue.md)
  The raw file-type bits from the C mode.
### Type Properties
- [static var blockSpecial: FileType](filetype/blockspecial.md)
  Block special device
- [static var characterSpecial: FileType](filetype/characterspecial.md)
  Character special device
- [static var directory: FileType](filetype/directory.md)
  Directory
- [static var fifo: FileType](filetype/fifo.md)
  FIFO (or named pipe)
- [static var regular: FileType](filetype/regular.md)
  Regular file
- [static var socket: FileType](filetype/socket.md)
  Socket
- [static var symbolicLink: FileType](filetype/symboliclink.md)
  Symbolic link
- [static var whiteout: FileType](filetype/whiteout.md)
  Whiteout file

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filetype)*