# recommendedAudioSettingsForAssetWriter(writingTo:)

**Framework**: AVFoundation  
**Kind**: method

Specifies the recommended settings for use with an `AVAssetWriterInput`.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func recommendedAudioSettingsForAssetWriter(writingTo outputFileType: AVFileType) -> [String : Any]?
```

#### Return Value

A fully populated dictionary of keys and values that are compatible with [`AVAssetWriter`](avassetwriter.md).

#### Discussion

The value of this property is an `NSDictionary` containing values for compression settings keys defined in [`Audio settings`](audio-settings.md). This dictionary is suitable for use as the [`assetWriterInputWithMediaType:outputSettings:`](avassetwriterinput/assetwriterinputwithmediatype:outputsettings:.md) method’s `outputSettings` parameter when creating an [`AVAssetWriterInputPixelBufferAdaptor`](avassetwriterinputpixelbufferadaptor.md); for example,

```objc
[AVAssetWriterInput assetWriterInputWithMediaType:AVMediaTypeAudio outputSettings:outputSettings sourceFormatHint:hint];
```

The dictionary returned contains all necessary keys and values needed to create an [`AVAssetWriter`](avassetwriter.md) instance; see the [`init(mediaType:outputSettings:)`](avassetwriterinput/init(mediatype:outputsettings:).md) method for a more in depth discussion. For QuickTime movie and ISO files, the recommended audio settings will always produce output comparable to that of [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md).

The dictionary of settings is dependent on the current configuration of the receiver’s [`AVCaptureSession`](avcapturesession.md) and its inputs. The settings dictionary may change if the session’s configuration changes. As such, you should configure your session first, then query the recommended audio settings.

## Parameters

- `outputFileType`: Specifies the UTI of the file type to be written. See   for the defined UTIs.

## See Also

- [var audioSettings: [String : Any]!](avcaptureaudiodataoutput/audiosettings.md)
  The settings used to decode or re-encode audio before it’s output.
- [var spatialAudioChannelLayoutTag: AudioChannelLayoutTag](avcaptureaudiodataoutput/spatialaudiochannellayouttag.md)
  The audio channel layout tag of the audio sample buffers produced by the audio data output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/recommendedaudiosettingsforassetwriter(writingto:))*