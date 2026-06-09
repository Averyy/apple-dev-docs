# capabilities

**Framework**: Now Playing  
**Kind**: property

The control capabilities this device supports.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let capabilities: [MediaDevice.Capability]
```

#### Discussion

Each value in the array describes one operation the device supports, built from a [`MediaDevice.Capability`](mediadevice/capability.md), such as [`absoluteVolume(_:onChange:)`](mediadevice/capability/absolutevolume(_:onchange:).md) or [`relativeVolume(onIncrement:onDecrement:)`](mediadevice/capability/relativevolume(onincrement:ondecrement:).md). Pass an empty array if the device exposes no controllable capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediadevice/capabilities)*