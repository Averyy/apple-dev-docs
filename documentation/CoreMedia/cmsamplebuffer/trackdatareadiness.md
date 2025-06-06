# trackDataReadiness(_:)

**Framework**: Core Media  
**Kind**: method

Associates a sample buffer’s data readiness with that of another sample buffer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func trackDataReadiness(_ sampleBufferToTrack: CMSampleBuffer) throws
```

#### Discussion

After calling this method, retrieving the value of the [`dataReadiness`](cmsamplebuffer/datareadiness-swift.property.md) property retrieves the value from the tracked sample buffer. Likewise, calling the [`makeDataReady()`](cmsamplebuffer/makedataready().md) method calls the tracked sample buffers method.

Use this method to convert a multi-sample buffer into single-sample buffer before the data is ready. The single-sample buffer tracks the data readiness of the multi-sample buffers.

## Parameters

- `sampleBufferToTrack`: The sample buffer for which to track readiness.

## See Also

- [var dataReadiness: CMSampleBuffer.DataReadiness](cmsamplebuffer/datareadiness-swift.property.md)
  A value that indicates the status of the data the sample buffer contains.
- [func setDataReadiness(CMSampleBuffer.DataReadiness) throws](cmsamplebuffer/setdatareadiness(_:).md)
  Sets the status of the sample buffer’s data.
- [CMSampleBuffer.DataReadiness](cmsamplebuffer/datareadiness-swift.enum.md)
  Constants that indicate the readiness of a sample buffer’s data.
- [func makeDataReady() throws](cmsamplebuffer/makedataready.md)
  Makes the sample buffer’s data ready for use by calling its handler closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/trackdatareadiness(_:))*