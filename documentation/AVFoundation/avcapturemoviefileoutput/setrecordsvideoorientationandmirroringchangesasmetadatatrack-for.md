# setRecordsVideoOrientationAndMirroringChangesAsMetadataTrack(_:for:)

**Framework**: AVFoundation  
**Kind**: method

Sets whether the movie file output creates a timed metadata track to capture changes to the connection’s video orientation and mirroring.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func setRecordsVideoOrientationAndMirroringChangesAsMetadataTrack(_ doRecordChanges: Bool, for connection: AVCaptureConnection)
```

## Parameters

- `doRecordChanges`: A Boolean value that indicates whether to capture orientation and mirroring information. The system observes this value only at the start of recording. Setting a different value has no effect until you start a new recording.
- `connection`: A connection that delivers video media to the movie file output. This method throws an invalid argument exception if the value isn’t a video connection or if the connection doesn’t terminate at the movie file output.

## See Also

- [func recordsVideoOrientationAndMirroringChangesAsMetadataTrack(for: AVCaptureConnection) -> Bool](avcapturemoviefileoutput/recordsvideoorientationandmirroringchangesasmetadatatrack(for:).md)
  A Boolean value that indicates whether the movie file output records video orientation and mirroring information as a metadata track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/setrecordsvideoorientationandmirroringchangesasmetadatatrack(_:for:))*