# MediaDevice.Capability

**Framework**: Now Playing  
**Kind**: struct

The control capabilities of a device.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct Capability
```

## Mentions

- [Publishing remote media sessions](publishing-remote-media-sessions.md)

#### Overview

Use this to specify what control operations a device supports. The system uses this information to enable or disable device-specific controls in the interface.

## Topics

### Type Methods
- [static func absoluteVolume(Float, onChange: (Float) async throws -> Void) -> MediaDevice.Capability](mediadevice/capability/absolutevolume(_:onchange:).md)
  Returns a capability that lets the device be set to a specific volume level.
- [static func relativeVolume(onIncrement: () async throws -> Void, onDecrement: () async throws -> Void) -> MediaDevice.Capability](mediadevice/capability/relativevolume(onincrement:ondecrement:).md)
  Returns a capability that lets the device increase or decrease its volume incrementally.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediadevice/capability)*