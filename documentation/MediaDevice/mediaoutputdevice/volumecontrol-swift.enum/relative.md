# MediaOutputDevice.VolumeControl.relative

**Framework**: Media Device  
**Kind**: case

Relative volume control is supported, [`changeVolume(by:for:)`](mediadeviceextension/changevolume(by:for:).md) must be used to change the volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case relative
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

The device only supports relative volume adjustments (up/down by increments). This is common with devices that have hardware volume buttons but do not expose their current volume level or allow direct volume setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/volumecontrol-swift.enum/relative)*