# CMSampleBufferMakeDataReady(_:)

**Framework**: Core Media  
**Kind**: func

Makes the sample buffer’s data ready for use by invoking its callback to load the data.

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
func CMSampleBufferMakeDataReady(_ sbuf: CMSampleBuffer) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

The `CMSampleBufferMakeDataReadyCallback` is passed in by the client during creation. It must return 0 if successful, and in that case, `CMSampleBufferMakeDataReady` sets the data readiness of the `CMSampleBuffer` to true. If the sample buffer isn’t ready, and there’s no `CMSampleBufferMakeDataReadyCallback` to call, `kCMSampleBufferError_BufferNotReady` will be returned. Similarly, if the `CMSampleBuffer` isn’t ready, and the `CMSampleBufferMakeDataReadyCallback` fails and returns an error, [`CMSampleBuffer`](cmsamplebuffer.md) will be returned.

## Parameters

- `sbuf`: The sample buffer being modified.

## See Also

- [func CMSampleBufferDataIsReady(CMSampleBuffer) -> Bool](cmsamplebufferdataisready(_:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data is ready for use.
- [func CMSampleBufferSetDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffersetdataready(_:).md)
  Marks a sample buffer’s data as ready for use.
- [func CMSampleBufferSetDataFailed(CMSampleBuffer, status: OSStatus) -> OSStatus](cmsamplebuffersetdatafailed(_:status:).md)
  Marks the sample buffer’s data as failed to indicate that it won’t become ready.
- [func CMSampleBufferHasDataFailed(CMSampleBuffer, statusOut: UnsafeMutablePointer<OSStatus>?) -> Bool](cmsamplebufferhasdatafailed(_:statusout:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data loading request failed.
- [func CMSampleBufferTrackDataReadiness(CMSampleBuffer, sampleBufferToTrack: CMSampleBuffer) -> OSStatus](cmsamplebuffertrackdatareadiness(_:samplebuffertotrack:).md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffermakedataready(_:))*