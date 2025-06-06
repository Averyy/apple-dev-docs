# CMSampleBuffer.DataReadiness.failed(_:)

**Framework**: Core Media  
**Kind**: case

The system failed to load the media data.

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
case failed(OSStatus)
```

## Parameters

- `status`: An   value that indicates the cause of the failure.

## See Also

- [CMSampleBuffer.DataReadiness.notReady](cmsamplebuffer/datareadiness-swift.enum/notready.md)
  The media data isn’t ready to use.
- [CMSampleBuffer.DataReadiness.ready](cmsamplebuffer/datareadiness-swift.enum/ready.md)
  The media data is ready to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/datareadiness-swift.enum/failed(_:))*