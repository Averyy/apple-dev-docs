# AVCaptureTimecodeGenerator.SynchronizationStatus.timedOut

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

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

```c
AVCaptureTimecodeGeneratorSynchronizationStatusTimedOut
```

## See Also

### Status values
- [AVCaptureTimecodeGenerator.SynchronizationStatus.notRequired](./notrequired.md)
  The timecode generator does not require active synchronization for a given source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceSelected](./sourceselected.md)
  A timecode source has been selected, but synchronization has not yet started.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceUnavailable](./sourceunavailable.md)
  The timecode generator has failed to establish a connection with a given source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.sourceUnsupported](./sourceunsupported.md)
  The timecode generator is receiving data from the source in an unrecognized format.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.synchronized](./synchronized.md)
  The timecode generator is successfully synchronized to the selected source, maintaining active timing alignment.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.synchronizing](./synchronizing.md)
  The timecode generator is actively synchronizing to the selected source.
- [AVCaptureTimecodeGenerator.SynchronizationStatus.unknown](./unknown.md)
  The initial state before a source is selected or during error conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/synchronizationstatus/timedout)*