# CMSampleBufferDataIsReady(_:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether the sample buffer’s data is ready for use.

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
func CMSampleBufferDataIsReady(_ sbuf: CMSampleBuffer) -> Bool
```

#### Return Value

A Boolean indicating whether or not the sample buffer’s data is ready.  True is returned for special marker buffers, even though they have no data. False is returned if there is an error.

## Parameters

- `sbuf`: The   being interrogated.

## See Also

- [func CMSampleBufferSetDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffersetdataready(_:).md)
  Marks a sample buffer’s data as ready for use.
- [func CMSampleBufferSetDataFailed(CMSampleBuffer, status: OSStatus) -> OSStatus](cmsamplebuffersetdatafailed(_:status:).md)
  Marks the sample buffer’s data as failed to indicate that it won’t become ready.
- [func CMSampleBufferHasDataFailed(CMSampleBuffer, statusOut: UnsafeMutablePointer<OSStatus>?) -> Bool](cmsamplebufferhasdatafailed(_:statusout:).md)
  Returns a Boolean value that indicates whether the sample buffer’s data loading request failed.
- [func CMSampleBufferMakeDataReady(CMSampleBuffer) -> OSStatus](cmsamplebuffermakedataready(_:).md)
  Makes the sample buffer’s data ready for use by invoking its callback to load the data.
- [func CMSampleBufferTrackDataReadiness(CMSampleBuffer, sampleBufferToTrack: CMSampleBuffer) -> OSStatus](cmsamplebuffertrackdatareadiness(_:samplebuffertotrack:).md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferdataisready(_:))*