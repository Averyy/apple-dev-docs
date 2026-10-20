# AXMFiHearingDevice.Ear

**Framework**: Accessibility  
**Kind**: struct  
**Role**: Structure

Constants that represent a hearing device ear.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Ear
```

```c
enum AXHearingDeviceEar : NSUInteger;
```

## Topics

### Constants
- [static var both: AXMFiHearingDevice.Ear](./ear/both.md)
  A constant that represents both ears.
- [static var left: AXMFiHearingDevice.Ear](./ear/left.md)
  A constant that represents the left ear.
- [static var right: AXMFiHearingDevice.Ear](./ear/right.md)
  A constant that represents the right ear.
### Initializer
- [init(rawValue: UInt)](./ear/init%28rawvalue%29.md)
  Creates a structure that represents a hearing device ear with the raw value you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Streaming status
- [static func streamingEar() -> AXMFiHearingDevice.Ear](./streamingear%28%29.md)
  Returns which ears enable streaming.
- [static let streamingEarDidChangeNotification: NSNotification.Name](./streamingeardidchangenotification.md)
  A notification that the system posts when there’s a change to which ears enable streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice/ear)*