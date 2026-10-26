# supportedMaxPhotoDimensions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The maximum photo dimension this format supports.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSValue *> * supportedMaxPhotoDimensions;
```

#### Discussion

The array contains [`NSValue`](../../Foundation/nsvalue.md) objects that hold a [`CMVideoDimensions`](../../CoreMedia/cmvideodimensions.md) structure.

## See Also

### Determining photo quality
- [var isHighPhotoQualitySupported: Bool](../avcapturedevice/format/ishighphotoqualitysupported.md)
  A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.
- [var isHighestPhotoQualitySupported: Bool](../avcapturedevice/format/ishighestphotoqualitysupported.md)
  A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/supportedmaxphotodimensions)*