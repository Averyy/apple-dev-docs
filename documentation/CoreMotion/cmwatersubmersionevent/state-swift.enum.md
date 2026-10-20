# CMWaterSubmersionEvent.State

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

The device’s submersion state.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum State
```

```c
enum CMWaterSubmersionState : NSInteger;
```

## Topics

### Submersion states
- [CMWaterSubmersionEvent.State.notSubmerged](./state-swift.enum/notsubmerged.md)
  The device isn’t submerged in water.
- [CMWaterSubmersionEvent.State.submerged](./state-swift.enum/submerged.md)
  The device is submerged in water.
- [CMWaterSubmersionEvent.State.unknown](./state-swift.enum/unknown.md)
  The submersion state is unknown.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing event data
- [var date: Date](./date.md)
  The time and date of the event.
- [var state: CMWaterSubmersionEvent.State](./state-swift.property.md)
  The new submersion state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionevent/state-swift.enum)*