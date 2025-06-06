# makeDataReady()

**Framework**: Core Media  
**Kind**: method

Makes the sample buffer’s data ready for use by calling its handler closure.

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
func makeDataReady() throws
```

## See Also

- [var dataReadiness: CMSampleBuffer.DataReadiness](cmsamplebuffer/datareadiness-swift.property.md)
  A value that indicates the status of the data the sample buffer contains.
- [func setDataReadiness(CMSampleBuffer.DataReadiness) throws](cmsamplebuffer/setdatareadiness(_:).md)
  Sets the status of the sample buffer’s data.
- [CMSampleBuffer.DataReadiness](cmsamplebuffer/datareadiness-swift.enum.md)
  Constants that indicate the readiness of a sample buffer’s data.
- [func trackDataReadiness(CMSampleBuffer) throws](cmsamplebuffer/trackdatareadiness(_:).md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/makedataready())*