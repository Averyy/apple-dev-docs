# dataReadiness

**Framework**: Core Media  
**Kind**: property

A value that indicates the status of the data the sample buffer contains.

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
var dataReadiness: CMSampleBuffer.DataReadiness { get }
```

## See Also

- [func setDataReadiness(CMSampleBuffer.DataReadiness) throws](cmsamplebuffer/setdatareadiness(_:).md)
  Sets the status of the sample buffer’s data.
- [CMSampleBuffer.DataReadiness](cmsamplebuffer/datareadiness-swift.enum.md)
  Constants that indicate the readiness of a sample buffer’s data.
- [func makeDataReady() throws](cmsamplebuffer/makedataready.md)
  Makes the sample buffer’s data ready for use by calling its handler closure.
- [func trackDataReadiness(CMSampleBuffer) throws](cmsamplebuffer/trackdatareadiness(_:).md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/datareadiness-swift.property)*