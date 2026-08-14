# Stat.Flags

**Framework**: System  
**Kind**: struct

Flags representing those passed to `fstatat()`.

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
struct Flags
```

## Topics

### Initializers
- [init(rawValue: CInt)](stat/flags-swift.struct/init(rawvalue:).md)
  Creates a strongly-typed `Stat.Flags` from raw C flags.
### Instance Properties
- [let rawValue: CInt](stat/flags-swift.struct/rawvalue.md)
  The raw C flags.
### Type Properties
- [static var resolveBeneath: Stat.Flags](stat/flags-swift.struct/resolvebeneath.md)
  If the path does not reside in the hierarchy beneath the starting directory, return an error.
- [static var symlinkNoFollow: Stat.Flags](stat/flags-swift.struct/symlinknofollow.md)
  If the path ends with a symbolic link, return information about the link itself.
- [static var symlinkNoFollowAny: Stat.Flags](stat/flags-swift.struct/symlinknofollowany.md)
  If the path ends with a symbolic link, return information about the link itself. If *any* symbolic link is encountered during path resolution, return an error.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [Hashable](../swift/hashable.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/stat/flags-swift.struct)*