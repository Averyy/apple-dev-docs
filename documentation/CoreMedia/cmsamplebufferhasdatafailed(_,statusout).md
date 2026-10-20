# CMSampleBufferHasDataFailed(_:statusOut:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the sample buffer’s data loading request failed.

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
func CMSampleBufferHasDataFailed(_ sbuf: CMSampleBuffer, statusOut: UnsafeMutablePointer<OSStatus>?) -> Bool
```

```c
extern Boolean CMSampleBufferHasDataFailed(CMSampleBufferRef sbuf, OSStatus *statusOut);
```

## Parameters

- `sbuf`: The `CMSampleBuffer` being interrogated.
- `statusOut`: Points to an `OSStatus` to receive a status code describing the failure. Pass `NULL` if you don’t want this information.

## See Also

### Determining Readiness
- [func CMSampleBufferDataIsReady(CMSampleBuffer) -> Bool](./cmsamplebufferdataisready%28_%29.md)
  Returns a Boolean value that indicates whether the sample buffer’s data is ready for use.
- [func CMSampleBufferSetDataReady(CMSampleBuffer) -> OSStatus](./cmsamplebuffersetdataready%28_%29.md)
  Marks a sample buffer’s data as ready for use.
- [func CMSampleBufferSetDataFailed(CMSampleBuffer, status: OSStatus) -> OSStatus](./cmsamplebuffersetdatafailed%28_,status%29.md)
  Marks the sample buffer’s data as failed to indicate that it won’t become ready.
- [func CMSampleBufferMakeDataReady(CMSampleBuffer) -> OSStatus](./cmsamplebuffermakedataready%28_%29.md)
  Makes the sample buffer’s data ready for use by invoking its callback to load the data.
- [func CMSampleBufferTrackDataReadiness(CMSampleBuffer, sampleBufferToTrack: CMSampleBuffer) -> OSStatus](./cmsamplebuffertrackdatareadiness%28_,samplebuffertotrack%29.md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferhasdatafailed(_:statusout:))*