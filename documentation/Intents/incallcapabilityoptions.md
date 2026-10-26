# INCallCapabilityOptions

**Framework**: Intents  
**Kind**: struct  
**Role**: Structure

Constants indicating the capabilities of the call.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
struct INCallCapabilityOptions
```

```c
enum INCallCapabilityOptions : NSUInteger;
```

## Topics

### Constants
- [static var audioCall: INCallCapabilityOptions](./incallcapabilityoptions/audiocall.md)
  An audio-only call.
- [static var videoCall: INCallCapabilityOptions](./incallcapabilityoptions/videocall.md)
  A video call.
### Initializers
- [init(rawValue: UInt)](./incallcapabilityoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallcapabilityoptions)*