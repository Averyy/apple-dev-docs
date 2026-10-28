# CNAssetSpatialAudioInfo

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```objc
@interface CNAssetSpatialAudioInfo : NSObject
```

## Overview

A helper class to inspect recordings made when Spatial Audio setting is turned on. An instance of this class contains the default audio track with Spatial Audio, metadata read from the file that can be applied during to enhance the playback experience. This class also provides tunable parameters to change the intensity & mode of the playback experience.

The goal of this class is to assist users operate on assets in which audio has been captured in multiple formats like Spatial Audio and Stereo to allow more audio customization. Users can audition playback of this asset with an immersive audio rendering effect applied by fetching an AVAudioMix containing the necessary metadata serialized in the file as well as any user supplied changes. Once the results of the audition are satisfactory, clients can create a copy of the asset with the audio effect burned in.

## Topics

### Instance Properties
- [defaultEffectIntensity](./cnassetspatialaudioinfo-57yc5/defaulteffectintensity.md)
- [defaultRenderingStyle](./cnassetspatialaudioinfo-57yc5/defaultrenderingstyle.md)
- [defaultSpatialAudioTrack](./cnassetspatialaudioinfo-57yc5/defaultspatialaudiotrack.md)
- [spatialAudioMixMetadata](./cnassetspatialaudioinfo-57yc5/spatialaudiomixmetadata.md)
### Instance Methods
- [- assetReaderOutputSettingsForContentType:](./cnassetspatialaudioinfo-57yc5/assetreaderoutputsettingsforcontenttype_.md)
- [- assetWriterInputSettingsForContentType:](./cnassetspatialaudioinfo-57yc5/assetwriterinputsettingsforcontenttype_.md)
- [- audioMixWithEffectIntensity:renderingStyle:](./cnassetspatialaudioinfo-57yc5/audiomixwitheffectintensity_renderingstyle_.md)
### Type Properties
- [isSupported](./cnassetspatialaudioinfo-57yc5/issupported.md)
### Type Methods
- [+ checkIfContainsSpatialAudio:completionHandler:](./cnassetspatialaudioinfo-57yc5/checkifcontainsspatialaudio_completionhandler_.md)
- [+ loadFromAsset:completionHandler:](./cnassetspatialaudioinfo-57yc5/loadfromasset_completionhandler_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetspatialaudioinfo-57yc5)*