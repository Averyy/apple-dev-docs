# MediaOutputDevice.VolumeControl.absolute

**Framework**: Media Device  
**Kind**: case

Full volume control is supported, [`setVolume(_:for:)`](mediadeviceextension/setvolume(_:for:).md) may be used to set the volume.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case absolute
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

The device supports absolute volume control, allowing direct setting of volume to specific levels (such as 0-100%). This provides the most precise volume control and enables features like volume sliders in the user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/volumecontrol-swift.enum/absolute)*