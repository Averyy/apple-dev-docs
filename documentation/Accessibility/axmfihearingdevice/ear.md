# AXMFiHearingDevice.Ear

**Framework**: Accessibility  
**Kind**: struct

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

## Topics

### Constants
- [static var both: AXMFiHearingDevice.Ear](axmfihearingdevice/ear/both.md)
  A constant that represents both ears.
- [static var left: AXMFiHearingDevice.Ear](axmfihearingdevice/ear/left.md)
  A constant that represents the left ear.
- [static var right: AXMFiHearingDevice.Ear](axmfihearingdevice/ear/right.md)
  A constant that represents the right ear.
### Initializer
- [init(rawValue: UInt)](axmfihearingdevice/ear/init(rawvalue:).md)
  Creates a structure that represents a hearing device ear with the raw value you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [static func streamingEar() -> AXMFiHearingDevice.Ear](axmfihearingdevice/streamingear.md)
  Returns which ears enable streaming.
- [static let streamingEarDidChangeNotification: NSNotification.Name](axmfihearingdevice/streamingeardidchangenotification.md)
  A notification that the system posts when there’s a change to which ears enable streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice/ear)*