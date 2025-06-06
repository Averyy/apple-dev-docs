# HMCharacteristicTypeImageRotation

**Framework**: HomeKit  
**Kind**: var

The angle of rotation for an image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let HMCharacteristicTypeImageRotation: String
```

#### Discussion

The corresponding value is a floating point number representing an angle in degrees that the image should be rotated. The only valid values are `0`, `90`, `180`, and `270`.

## See Also

- [let HMCharacteristicTypeSupportedRTPConfiguration: String](hmcharacteristictypesupportedrtpconfiguration.md)
  The supported Real-time Transport Protocol (RTP) configuration.
- [let HMCharacteristicTypeDigitalZoom: String](hmcharacteristictypedigitalzoom.md)
  The digital zoom of a video Real-time Transport Protocol (RTP) service.
- [let HMCharacteristicTypeOpticalZoom: String](hmcharacteristictypeopticalzoom.md)
  The optical zoom setting of the camera sourcing a video Real-time Transport Protocol (RTP) service.
- [let HMCharacteristicTypeImageMirroring: String](hmcharacteristictypeimagemirroring.md)
  An indicator of whether the image should be flipped about the vertical axis.
- [let HMCharacteristicTypeNightVision: String](hmcharacteristictypenightvision.md)
  An indicator of whether night vision is enabled on a video Real-time Transport Protocol (RTP) service.
- [let HMCharacteristicTypeStreamingStatus: String](hmcharacteristictypestreamingstatus.md)
  A description of the status of the Real-time Transport Protocol (RTP) stream management service.
- [let HMCharacteristicTypeSupportedVideoStreamConfiguration: String](hmcharacteristictypesupportedvideostreamconfiguration.md)
  The video stream’s configuration.
- [let HMCharacteristicTypeSupportedAudioStreamConfiguration: String](hmcharacteristictypesupportedaudiostreamconfiguration.md)
  The audio stream’s configuration.
- [let HMCharacteristicTypeSelectedStreamConfiguration: String](hmcharacteristictypeselectedstreamconfiguration.md)
  The selected stream’s configuration.
- [let HMCharacteristicTypeSetupStreamEndpoint: String](hmcharacteristictypesetupstreamendpoint.md)
  The stream’s endpoint configuration.
- [let HMCharacteristicTypeAudioFeedback: String](hmcharacteristictypeaudiofeedback.md)
  An indicator of whether audio feedback, like a beep or other external sound mechanism, is enabled.
- [let HMCharacteristicTypeVolume: String](hmcharacteristictypevolume.md)
  The input or output volume of an audio device.
- [let HMCharacteristicTypeMute: String](hmcharacteristictypemute.md)
  A control for muting audio.
- [let HMCharacteristicTypeVolumeSelector: String](hmcharacteristictypevolumeselector.md)
  The mechanism to increment or decrement the volume by the default step value.
- [let HMCharacteristicTypeVolumeControlType: String](hmcharacteristictypevolumecontroltype.md)
  The volume control capabilities of an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypeimagerotation)*