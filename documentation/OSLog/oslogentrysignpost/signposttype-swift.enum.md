# OSLogEntrySignpost.SignpostType

**Framework**: OSLog  
**Kind**: enum  
**Role**: Enumeration

The available signpost types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum SignpostType
```

```c
enum OSLogEntrySignpostType : NSInteger;
```

## Topics

### Enumeration Cases
- [OSLogEntrySignpost.SignpostType.undefined](./signposttype-swift.enum/undefined.md)
  The signpost does not have a type.
- [OSLogEntrySignpost.SignpostType.intervalBegin](./signposttype-swift.enum/intervalbegin.md)
  The signpost marks the start of a time interval.
- [OSLogEntrySignpost.SignpostType.intervalEnd](./signposttype-swift.enum/intervalend.md)
  The signpost marks the end of a time interval.
- [OSLogEntrySignpost.SignpostType.event](./signposttype-swift.enum/event.md)
  The signpost marks an event.
### Initializers
- [init?(rawValue: Int)](./signposttype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing Signpost Types
- [var signpostType: OSLogEntrySignpost.SignpostType](./signposttype-swift.property.md)
  The signpost’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentrysignpost/signposttype-swift.enum)*