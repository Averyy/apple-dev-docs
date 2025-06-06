# CMSampleBuffer.DataReadiness

**Framework**: Core Media  
**Kind**: enum

Constants that indicate the readiness of a sample buffer’s data.

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
enum DataReadiness
```

## Topics

### States
- [CMSampleBuffer.DataReadiness.notReady](cmsamplebuffer/datareadiness-swift.enum/notready.md)
  The media data isn’t ready to use.
- [CMSampleBuffer.DataReadiness.ready](cmsamplebuffer/datareadiness-swift.enum/ready.md)
  The media data is ready to use.
- [CMSampleBuffer.DataReadiness.failed(_:)](cmsamplebuffer/datareadiness-swift.enum/failed(_:).md)
  The system failed to load the media data.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var dataReadiness: CMSampleBuffer.DataReadiness](cmsamplebuffer/datareadiness-swift.property.md)
  A value that indicates the status of the data the sample buffer contains.
- [func setDataReadiness(CMSampleBuffer.DataReadiness) throws](cmsamplebuffer/setdatareadiness(_:).md)
  Sets the status of the sample buffer’s data.
- [func makeDataReady() throws](cmsamplebuffer/makedataready.md)
  Makes the sample buffer’s data ready for use by calling its handler closure.
- [func trackDataReadiness(CMSampleBuffer) throws](cmsamplebuffer/trackdatareadiness(_:).md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/datareadiness-swift.enum)*