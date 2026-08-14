# GroupID

**Framework**: System  
**Kind**: struct

A Swift wrapper of the C `gid_t` type.

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
struct GroupID
```

## Topics

### Initializers
- [init(CInterop.GroupID)](groupid/init(_:).md)
  Creates a strongly-typed `GroupID` from the raw C value.
- [init(rawValue: CInterop.GroupID)](groupid/init(rawvalue:).md)
  Creates a strongly-typed `GroupID` from the raw C value.
### Instance Properties
- [var rawValue: CInterop.GroupID](groupid/rawvalue.md)
  The raw C `gid_t`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/system/groupid)*