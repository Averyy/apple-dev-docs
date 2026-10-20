# timecodeGenerator(_:didUpdateAvailableSources:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate when the list of available timecode synchronization sources is updated.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func timecodeGenerator(_ generator: AVCaptureTimecodeGenerator, didUpdateAvailableSources availableSources: [AVCaptureTimecode.Source])
```

```objc
- (void) timecodeGenerator:(AVCaptureTimecodeGenerator *) generator didUpdateAvailableSources:(NSArray<AVCaptureTimecodeSource *> *) availableSources;
```

## Parameters

- `generator`: The [`AVCaptureTimecodeGenerator`](../avcapturetimecodegenerator.md) instance providing the source list update.
- `availableSources`: An array of [`AVCaptureTimecode.Source`](../avcapturetimecode/source.md) objects representing the available timecode synchronization sources.

## See Also

### Responding to timecode events
- [func timecodeGenerator(AVCaptureTimecodeGenerator, didReceiveUpdate: AVCaptureTimecode, from: AVCaptureTimecode.Source)](./timecodegenerator%28_,didreceiveupdate,from%29.md)
  Notifies the delegate when new, unaligned timecodes are parsed from the specified source.
- [func timecodeGenerator(AVCaptureTimecodeGenerator, transitionedTo: AVCaptureTimecodeGenerator.SynchronizationStatus, for: AVCaptureTimecode.Source)](./timecodegenerator%28_,transitionedto,for%29.md)
  Notifies the delegate when the synchronization status of a timecode source changes.
- [AVCaptureTimecodeGenerator.SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:didupdateavailablesources:))*