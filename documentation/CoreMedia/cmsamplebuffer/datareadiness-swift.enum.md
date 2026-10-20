# CMSampleBuffer.DataReadiness

**Framework**: Core Media  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the readiness of a sample buffer’s data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
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
- [CMSampleBuffer.DataReadiness.notReady](./datareadiness-swift.enum/notready.md)
  The media data isn’t ready to use.
- [CMSampleBuffer.DataReadiness.ready](./datareadiness-swift.enum/ready.md)
  The media data is ready to use.
- [CMSampleBuffer.DataReadiness.failed(_:)](./datareadiness-swift.enum/failed%28_%29.md)
  The system failed to load the media data.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Determining Readiness
- [var dataReadiness: CMSampleBuffer.DataReadiness](./datareadiness-swift.property.md)
  A value that indicates the status of the data the sample buffer contains.
- [func setDataReadiness(CMSampleBuffer.DataReadiness) throws](./setdatareadiness%28_%29.md)
  Sets the status of the sample buffer’s data.
- [func makeDataReady() throws](./makedataready%28%29.md)
  Makes the sample buffer’s data ready for use by calling its handler closure.
- [func trackDataReadiness(CMSampleBuffer) throws](./trackdatareadiness%28_%29.md)
  Associates a sample buffer’s data readiness with that of another sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/datareadiness-swift.enum)*