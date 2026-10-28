# capabilities

**Framework**: Now Playing  
**Kind**: property  
**Role**: Instance Property

The control capabilities this device supports.

**Availability**:
- iOS 27.0+
- iOS App Extension 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
let capabilities: [MediaDevice.Capability]
```

## Discussion

Each value in the array describes one operation the device supports, built from a [`MediaDevice.Capability`](./capability.md), such as [`absoluteVolume(_:onChange:)`](./capability/absolutevolume%28_,onchange%29.md) or [`relativeVolume(onIncrement:onDecrement:)`](./capability/relativevolume%28onincrement,ondecrement%29.md). Pass an empty array if the device exposes no controllable capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediadevice/capabilities)*