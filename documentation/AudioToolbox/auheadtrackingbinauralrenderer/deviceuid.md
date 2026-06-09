# deviceUID

**Framework**: Audio Toolbox  
**Kind**: property

The Unique Identifier (UID) of the Bluetooth headphone device providing IMU sensor data for head tracking.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var deviceUID: String? { get }
```

## Mentions

- [Rendering Spatial Audio from Bluetooth headphones](rendering-spatial-audio-from-bluetooth-headphones.md)

#### Discussion

The UID identifies which Bluetooth headphone device corresponds to this instance of the Audio Unit. The host sets this property when it matches a device with this instance of the Audio Unit.

The Audio Unit should monitor this property to detect when the host matches the Audio Unit with Bluetooth headphones.

This property supports Key-Value Observing (KVO).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auheadtrackingbinauralrenderer/deviceuid)*