# AVCaptureTimecodeGenerator.SynchronizationStatus.timedOut

**Framework**: AVFoundation  
**Kind**: case

The synchronization has timed out.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
case timedOut
```

## See Also

- [AVCaptureTimecodeGenerator.SynchronizationStatus.notRequired](avcapturetimecodegenerator/synchronizationstatus/notrequired.md)
  The timecode generator does not require active synchronization for a given source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceSelected](avcapturetimecodegenerator/synchronizationstatus/sourceselected.md)
  A timecode source has been selected, but synchronization has not yet started.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceUnavailable](avcapturetimecodegenerator/synchronizationstatus/sourceunavailable.md)
  The timecode generator has failed to establish a connection with a given source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceUnsupported](avcapturetimecodegenerator/synchronizationstatus/sourceunsupported.md)
  The timecode generator is receiving data from the source in an unrecognized format.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.synchronized](avcapturetimecodegenerator/synchronizationstatus/synchronized.md)
  The timecode generator is successfully synchronized to the selected source, maintaining active timing alignment.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.synchronizing](avcapturetimecodegenerator/synchronizationstatus/synchronizing.md)
  The timecode generator is actively synchronizing to the selected source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.unknown](avcapturetimecodegenerator/synchronizationstatus/unknown.md)
  The initial state before a source is selected or during error conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus/timedout)*