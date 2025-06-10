# OSLogEntrySignpost.SignpostType

**Framework**: OSLog  
**Kind**: enum

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

## Topics

### Enumeration Cases
- [OSLogEntrySignpost.SignpostType.undefined](oslogentrysignpost/signposttype-swift.enum/undefined.md)
  The signpost does not have a type.
- [OSLogEntrySignpost.SignpostType.intervalBegin](oslogentrysignpost/signposttype-swift.enum/intervalbegin.md)
  The signpost marks the start of a time interval.
- [OSLogEntrySignpost.SignpostType.intervalEnd](oslogentrysignpost/signposttype-swift.enum/intervalend.md)
  The signpost marks the end of a time interval.
- [OSLogEntrySignpost.SignpostType.event](oslogentrysignpost/signposttype-swift.enum/event.md)
  The signpost marks an event.
### Initializers
- [init?(rawValue: Int)](oslogentrysignpost/signposttype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var signpostType: OSLogEntrySignpost.SignpostType](oslogentrysignpost/signposttype-swift.property.md)
  The signpost’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogentrysignpost/signposttype-swift.enum)*