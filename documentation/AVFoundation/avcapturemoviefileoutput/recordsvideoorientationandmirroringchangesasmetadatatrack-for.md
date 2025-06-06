# recordsVideoOrientationAndMirroringChangesAsMetadataTrack(for:)

**Framework**: AVFoundation  
**Kind**: method

A Boolean value that indicates whether the movie file output records video orientation and mirroring information as a metadata track.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func recordsVideoOrientationAndMirroringChangesAsMetadataTrack(for connection: AVCaptureConnection) -> Bool
```

## Parameters

- `connection`: A connection delivering video media to the movie file output. This method throws an invalid argument exception if the value isn’t a video connection or if the connection doesn’t terminate at the movie file output.

## See Also

- [func setRecordsVideoOrientationAndMirroringChangesAsMetadataTrack(Bool, for: AVCaptureConnection)](avcapturemoviefileoutput/setrecordsvideoorientationandmirroringchangesasmetadatatrack(_:for:).md)
  Sets whether the movie file output creates a timed metadata track to capture changes to the connection’s video orientation and mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/recordsvideoorientationandmirroringchangesasmetadatatrack(for:))*