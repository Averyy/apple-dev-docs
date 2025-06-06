# AXMFiHearingDevice

**Framework**: Accessibility  
**Kind**: struct

A namespace for hearing device accessibility symbols in Swift.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct AXMFiHearingDevice
```

## Topics

### Streaming status
- [static func streamingEar() -> AXMFiHearingDevice.Ear](axmfihearingdevice/streamingear.md)
  Returns which ears enable streaming.
- [AXMFiHearingDevice.Ear](axmfihearingdevice/ear.md)
  Constants that represent a hearing device ear.
- [static let streamingEarDidChangeNotification: NSNotification.Name](axmfihearingdevice/streamingeardidchangenotification.md)
  A notification that the system posts when there’s a change to which ears enable streaming.
### Streaming type
- [static func supportsBidirectionalStreaming() -> Bool](axmfihearingdevice/supportsbidirectionalstreaming.md)
  Returns a Boolean value that indicates whether the iOS device supports bidirectional streaming.
### Paired hearing devices
- [static func pairedDeviceIdentifiers() -> [UUID]](axmfihearingdevice/paireddeviceidentifiers.md)
  Returns the UUIDs of the hearing device peripherals.
- [static let pairedUUIDsDidChangeNotification: NSNotification.Name](axmfihearingdevice/paireduuidsdidchangenotification.md)
  A notification that the system posts when there’s a change to the UUIDs of the hearing device peripherals.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axmfihearingdevice)*