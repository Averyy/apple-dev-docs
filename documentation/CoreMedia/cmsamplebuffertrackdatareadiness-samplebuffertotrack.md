# CMSampleBufferTrackDataReadiness(_:sampleBufferToTrack:)

**Framework**: Core Media  
**Kind**: func

Associates a sample buffer’s data readiness with that of another sample buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSampleBufferTrackDataReadiness(_ sbuf: CMSampleBuffer, sampleBufferToTrack: CMSampleBuffer) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

After calling this API, if `CMSampleBufferDataIsReady` is called, it will return `sampleBufferToTrack`’s data readiness. If `CMSampleBufferMakeDataReady` is called, it will make `sampleBufferToTrack` data ready.

Example of use: This allows bursting a multi-sample `CMSampleBuffer` into single-sample `CMSampleBuffers` before the data is ready. The single-sample `CMSampleBuffers` will all track the multi-sample `CMSampleBuffer’s` data readiness.

## Parameters

- `sbuf`: The sample buffer being modified.
- `sampleBufferToTrack`: The sample buffer being tracked.

## See Also

- [func CMSampleBufferDataIsReady(CMSampleBuffer) -> Bool](cmsamplebufferdataisready(_:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data is ready for use.
- [func CMSampleBufferSetDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffersetdataready(_:).md)
  Marks a sample buffer’s data as ready for use.
- [func CMSampleBufferSetDataFailed(CMSampleBuffer, status: OSStatus) -> OSStatus](cmsamplebuffersetdatafailed(_:status:).md)
  Marks the sample buffer’s data as failed to indicate that it won’t become ready.
- [func CMSampleBufferHasDataFailed(CMSampleBuffer, statusOut: UnsafeMutablePointer<OSStatus>?) -> Bool](cmsamplebufferhasdatafailed(_:statusout:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data loading request failed.
- [func CMSampleBufferMakeDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffermakedataready(_:).md)
  Makes the sample buffer’s data ready for use by invoking its callback to load the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffertrackdatareadiness(_:samplebuffertotrack:))*