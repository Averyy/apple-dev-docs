# CMSampleBufferSetDataReady(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Marks a sample buffer’s data as ready for use.

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
func CMSampleBufferSetDataReady(_ sbuf: CMSampleBuffer) -> OSStatus
```

```c
extern OSStatus CMSampleBufferSetDataReady(CMSampleBufferRef sbuf);
```

#### Return Value

A result code. See [Sample Buffer Error Codes](./sample-buffer-errors.md).

#### Discussion

There’s no way to undo this operation. The only way to get an “unready” `CMSampleBuffer` is to call `CMSampleBufferCreate` with the `dataReady` parameter set to `false`.

## Parameters

- `sbuf`: The sample buffer being modified.

## See Also

### Determining Readiness
- [func CMSampleBufferDataIsReady(CMSampleBuffer) -> Bool](./cmsamplebufferdataisready%28_%29.md)
  Returns a Boolean value that indicates whether the sample buffer’s data is ready for use.
- [func CMSampleBufferSetDataFailed(CMSampleBuffer, status: OSStatus) -> OSStatus](./cmsamplebuffersetdatafailed%28_,status%29.md)
  Marks the sample buffer’s data as failed to indicate that it won’t become ready.
- [func CMSampleBufferHasDataFailed(CMSampleBuffer, statusOut: UnsafeMutablePointer<OSStatus>?) -> Bool](./cmsamplebufferhasdatafailed%28_,statusout%29.md)
  Returns a Boolean value that indicates whether the sample buffer’s data loading request failed.
- [func CMSampleBufferMakeDataReady(CMSampleBuffer) -> OSStatus](./cmsamplebuffermakedataready%28_%29.md)
  Makes the sample buffer’s data ready for use by invoking its callback to load the data.
- [func CMSampleBufferTrackDataReadiness(CMSampleBuffer, sampleBufferToTrack: CMSampleBuffer) -> OSStatus](./cmsamplebuffertrackdatareadiness%28_,samplebuffertotrack%29.md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetdataready(_:))*