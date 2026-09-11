# Inode

**Framework**: System  
**Kind**: struct

A Swift wrapper of the C `ino_t` type.

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
struct Inode
```

## Topics

### Initializers
- [init(CInterop.Inode)](inode/init(_:).md)
  Creates a strongly-typed `Inode` from the raw C value.
- [init(rawValue: CInterop.Inode)](inode/init(rawvalue:).md)
  Creates a strongly-typed `Inode` from the raw C value.
### Instance Properties
- [var rawValue: CInterop.Inode](inode/rawvalue.md)
  The raw C `ino_t`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/system/inode)*