# CMSampleBufferDataIsReady(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern Boolean CMSampleBufferDataIsReady(CMSampleBufferRef sbuf);
```

## Return Value

A Boolean indicating whether or not the sample buffer’s data is ready.  True is returned for special marker buffers, even though they have no data. False is returned if there is an error.

## Parameters

- `sbuf`: The `CMSampleBuffer` being interrogated.

## See Also

### Determining Readiness
- [func CMSampleBufferSetDataReady(CMSampleBuffer) -> OSStatus](./cmsamplebuffersetdataready%28_%29.md)
  Marks a sample buffer’s data as ready for use.
- [func CMSampleBufferSetDataFailed(CMSampleBuffer, status: OSStatus) -> OSStatus](./cmsamplebuffersetdatafailed%28_,status%29.md)
  Marks the sample buffer’s data as failed to indicate that it won’t become ready.
- [func CMSampleBufferHasDataFailed(CMSampleBuffer, statusOut: UnsafeMutablePointer<OSStatus>?) -> Bool](./cmsamplebufferhasdatafailed%28_,statusout%29.md)
  Returns a Boolean value that indicates whether the sample buffer’s data loading request failed.
- [func CMSampleBufferMakeDataReady(CMSampleBuffer) -> OSStatus](./cmsamplebuffermakedataready%28_%29.md)
  Makes the sample buffer’s data ready for use by invoking its callback to load the data.
- [func CMSampleBufferTrackDataReadiness(CMSampleBuffer, sampleBufferToTrack: CMSampleBuffer) -> OSStatus](./cmsamplebuffertrackdatareadiness%28_,samplebuffertotrack%29.md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferdataisready(_:))*