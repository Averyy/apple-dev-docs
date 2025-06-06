# CMSampleBufferSetDataFailed(_:status:)

**Framework**: Core Media  
**Kind**: func

Marks the sample buffer’s data as failed to indicate that it won’t become ready.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSampleBufferSetDataFailed(_ sbuf: CMSampleBuffer, status: OSStatus) -> OSStatus
```

## Parameters

- `sbuf`: The   being modified.
- `status`: A status describing the failure.

## See Also

- [func CMSampleBufferDataIsReady(CMSampleBuffer) -> Bool](cmsamplebufferdataisready(_:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data is ready for use.
- [func CMSampleBufferSetDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffersetdataready(_:).md)
  Marks a sample buffer’s data as ready for use.
- [func CMSampleBufferHasDataFailed(CMSampleBuffer, statusOut: UnsafeMutablePointer<OSStatus>?) -> Bool](cmsamplebufferhasdatafailed(_:statusout:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data loading request failed.
- [func CMSampleBufferMakeDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffermakedataready(_:).md)
  Makes the sample buffer’s data ready for use by invoking its callback to load the data.
- [func CMSampleBufferTrackDataReadiness(CMSampleBuffer, sampleBufferToTrack: CMSampleBuffer) -> OSStatus](cmsamplebuffertrackdatareadiness(_:samplebuffertotrack:).md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetdatafailed(_:status:))*