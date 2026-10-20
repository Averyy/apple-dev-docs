# GroupID

**Framework**: System  
**Kind**: struct  
**Role**: Structure

A Swift wrapper of the C `gid_t` type.

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
struct GroupID
```

## Topics

### Initializers
- [init(CInterop.GroupID)](./groupid/init%28_%29.md)
  Creates a strongly-typed `GroupID` from the raw C value.
- [init(rawValue: CInterop.GroupID)](./groupid/init%28rawvalue%29.md)
  Creates a strongly-typed `GroupID` from the raw C value.
### Instance Properties
- [var rawValue: CInterop.GroupID](./groupid/rawvalue.md)
  The raw C `gid_t`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/system/groupid)*