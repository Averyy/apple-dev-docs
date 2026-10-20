# timecodeGenerator(_:transitionedTo:for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate when the synchronization status of a timecode source changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func timecodeGenerator(_ generator: AVCaptureTimecodeGenerator, transitionedTo synchronizationStatus: AVCaptureTimecodeGenerator.SynchronizationStatus, for source: AVCaptureTimecode.Source)
```

```objc
- (void) timecodeGenerator:(AVCaptureTimecodeGenerator *) generator transitionedToSynchronizationStatus:(AVCaptureTimecodeGeneratorSynchronizationStatus) synchronizationStatus forSource:(AVCaptureTimecodeSource *) source;
```

## Parameters

- `generator`: The [`AVCaptureTimecodeGenerator`](../avcapturetimecodegenerator.md) instance providing the status update.
- `synchronizationStatus`: The updated synchronization state.
- `source`: The internal or external source to which the generator synchronizes.

## See Also

### Responding to timecode events
- [func timecodeGenerator(AVCaptureTimecodeGenerator, didReceiveUpdate: AVCaptureTimecode, from: AVCaptureTimecode.Source)](./timecodegenerator%28_,didreceiveupdate,from%29.md)
  Notifies the delegate when new, unaligned timecodes are parsed from the specified source.
- [func timecodeGenerator(AVCaptureTimecodeGenerator, didUpdateAvailableSources: [AVCaptureTimecode.Source])](./timecodegenerator%28_,didupdateavailablesources%29.md)
  Notifies the delegate when the list of available timecode synchronization sources is updated.
- [AVCaptureTimecodeGenerator.SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:transitionedto:for:))*