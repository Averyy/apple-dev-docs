# Stat.Flags

**Framework**: System  
**Kind**: struct  
**Role**: Structure

Flags representing those passed to `fstatat()`.

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
struct Flags
```

## Topics

### Initializers
- [init(rawValue: CInt)](./flags-swift.struct/init%28rawvalue%29.md)
  Creates a strongly-typed `Stat.Flags` from raw C flags.
### Instance Properties
- [let rawValue: CInt](./flags-swift.struct/rawvalue.md)
  The raw C flags.
### Type Properties
- [static var resolveBeneath: Stat.Flags](./flags-swift.struct/resolvebeneath.md)
  If the path does not reside in the hierarchy beneath the starting directory, return an error.
- [static var symlinkNoFollow: Stat.Flags](./flags-swift.struct/symlinknofollow.md)
  If the path ends with a symbolic link, return information about the link itself.
- [static var symlinkNoFollowAny: Stat.Flags](./flags-swift.struct/symlinknofollowany.md)
  If the path ends with a symbolic link, return information about the link itself. If *any* symbolic link is encountered during path resolution, return an error.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/flags-swift.struct)*