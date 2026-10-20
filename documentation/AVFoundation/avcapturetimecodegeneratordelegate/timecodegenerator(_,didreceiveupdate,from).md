# timecodeGenerator(_:didReceiveUpdate:from:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Notifies the delegate when new, unaligned timecodes are parsed from the specified source.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func timecodeGenerator(_ generator: AVCaptureTimecodeGenerator, didReceiveUpdate timecode: AVCaptureTimecode, from source: AVCaptureTimecode.Source)
```

```objc
- (void) timecodeGenerator:(AVCaptureTimecodeGenerator *) generator didReceiveUpdate:(AVCaptureTimecode) timecode fromSource:(AVCaptureTimecodeSource *) source;
```

## Parameters

- `generator`: The timecode generator providing the update.
- `timecode`: The updated timecode data.
- `source`: The source from which the timecode was received.

## See Also

### Responding to timecode events
- [func timecodeGenerator(AVCaptureTimecodeGenerator, didUpdateAvailableSources: [AVCaptureTimecode.Source])](./timecodegenerator%28_,didupdateavailablesources%29.md)
  Notifies the delegate when the list of available timecode synchronization sources is updated.
- [func timecodeGenerator(AVCaptureTimecodeGenerator, transitionedTo: AVCaptureTimecodeGenerator.SynchronizationStatus, for: AVCaptureTimecode.Source)](./timecodegenerator%28_,transitionedto,for%29.md)
  Notifies the delegate when the synchronization status of a timecode source changes.
- [AVCaptureTimecodeGenerator.SynchronizationStatus](../avcapturetimecodegenerator/synchronizationstatus.md)
  Constants defining the synchronization status of a timecode generator .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegeneratordelegate/timecodegenerator(_:didreceiveupdate:from:))*