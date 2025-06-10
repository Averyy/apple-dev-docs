# Editing Spatial Audio with an audio mix

**Framework**: Cinematic

Add Spatial Audio editing capabilities with the Audio Mix API in the Cinematic framework.

**Availability**:
- macOS 26.0+ (Beta)
- Xcode 26.0+ (Beta)

#### Overview

Beginning with iPhone 16, you can use Spatial Audio capture to record video with 3D audio, and edit the audio mix in the Photos app. With Audio Mix, you have creative control of the background and foreground sounds in a recording. It isolates speech as foreground and ambience as background, and you can select between multiple creative rendering styles to adjust the mix.

The `SpatialAudioCLI` sample project is a command-line tool that demonstrates three different methods for applying an audio mix: using [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer), using [`AVAssetWriter`](https://developer.apple.com/documentation/AVFoundation/AVAssetWriter), and using [`kAudioUnitSubType_AUAudioMix`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitSubType_AUAudioMix).

> **Note**: This sample code project is associated with WWDC25 session 251: [`Enhance your app’s audio content creation capabilities`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/251).

##### Configure the Sample Code Project

For best results, use `SpatialAudioCLI` with media that contains a Spatial Audio track. On all iPhone 16 models, Spatial Audio recording is available when capturing video with the Camera app. See the [`iPhone User Guide`](https://developer.apple.comhttps://support.apple.com/en-kw/guide/iphone/iph31c1ca6c7/ios) for how to change sound recording options.

You can record Spatial Audio in your app by setting the [`multichannelAudioMode`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDeviceInput/multichannelAudioMode) property of the [`AVCaptureDeviceInput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDeviceInput) to a value of `firstOrderAmbisonics`.

##### Adjust the Audio Mix in Avplayer

The simplest way to adjust the audio mix is to play Spatial Audio assets with [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer).

First, the sample loads the specified input file into an [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem):

```swift
let myAsset = AVURLAsset(url: URL(filePath: "myMediaURL"))
let myPlayerItem = AVPlayerItem(asset: myAsset)
```

Then the sample uses the [`AVAsset`](https://developer.apple.com/documentation/AVFoundation/AVAsset) to initialize an instance of `CNAssetSpatialAudioInfo`:

```swift
do {
    // This command throws if the input file does not have proper Spatial Audio.
    let audioInfo = try await CNAssetSpatialAudioInfo(asset: myAsset)
} catch {
    print("A problem occured reading the spatial audio asset: \(error)")
}
```

The two primary mix parameters are `effectIntensity` and `renderingStyle`. The sample creates an [`AVAudioMix`](https://developer.apple.com/documentation/AVFoundation/AVAudioMix) with the specified mix parameters and sets it on the [`AVPlayerItem`](https://developer.apple.com/documentation/AVFoundation/AVPlayerItem):

```swift
// Sets the mix parameters.
let intensity = 0.5 // Float values between 0.0 and 1.0.
let style = CNSpatialAudioRenderingStyle.cinematic

// Creates an `AVAudioMix` with effect intensity and rendering style.   
let newAudioMix = audioInfo.audioMix(effectIntensity: intensity, renderingStyle: style)
myPlayerItem.audioMix = newAudioMix

// AVPlayer plays the asset with the new audio mix parameters.
let player = AVPlayer(playerItem: myPlayerItem)
```

## See Also

- [struct CNDetection](cndetection-swift.struct.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [struct CNDecision](cndecision-swift.struct.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [class CNDetectionTrack](cndetectiontrack-2bxtd.md)
  An object representing a series of detections of the same subject over time.
- [class CNFixedDetectionTrack](cnfixeddetectiontrack-93rrw.md)
  An object representing the fixed detection track.
- [class CNCustomDetectionTrack](cncustomdetectiontrack-9a2zo.md)
  An object representing a discrete detection track composed of individual detections.
- [enum CNDetectionType](cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/editing-spatial-audio-with-an-audio-mix)*