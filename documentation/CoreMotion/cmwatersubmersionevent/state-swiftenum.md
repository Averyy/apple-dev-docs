# CMWaterSubmersionEvent.State

**Framework**: Core Motion  
**Kind**: enum

The device’s submersion state.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum State
```

## Topics

### Submersion states
- [CMWaterSubmersionEvent.State.notSubmerged](cmwatersubmersionevent/state-swift.enum/notsubmerged.md)
  The device isn’t submerged in water.
- [CMWaterSubmersionEvent.State.submerged](cmwatersubmersionevent/state-swift.enum/submerged.md)
  The device is submerged in water.
- [CMWaterSubmersionEvent.State.unknown](cmwatersubmersionevent/state-swift.enum/unknown.md)
  The submersion state is unknown.
### Initializers
- [init?(rawValue: Int)](cmwatersubmersionevent/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var date: Date](cmwatersubmersionevent/date.md)
  The time and date of the event.
- [var state: CMWaterSubmersionEvent.State](cmwatersubmersionevent/state-swift.property.md)
  The new submersion state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum)*