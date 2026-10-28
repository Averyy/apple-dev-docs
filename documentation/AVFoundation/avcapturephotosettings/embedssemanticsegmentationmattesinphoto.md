# embedsSemanticSegmentationMattesInPhoto

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether to write the enabled semantic segmentation matte types captured with this photo to the photo’s file structure.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var embedsSemanticSegmentationMattesInPhoto: Bool { get set }
```

```objc
@property (nonatomic) BOOL embedsSemanticSegmentationMattesInPhoto;
```

## Discussion

Semantic segmentation mattes are only supported in HEIF and JPEG. The photo output ignores this property if you set [`enabledSemanticSegmentationMatteTypes`](./enabledsemanticsegmentationmattetypes.md) to an empty array.

The property’s default value is [`true`](../../Swift/true.md).

> ❗ **Important**:  Enabling semantic segmentation matte delivery requires a lengthy reconfiguration of the capture render pipeline. If you intend to capture semantic segmentation mattes, set this property to [`true`](../../Swift/true.md) before calling the capture session’s [`startRunning()`](../avcapturesession/startrunning%28%29.md) method.

## See Also

### Capturing semantic segmentation mattes
- [var enabledSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType]](./enabledsemanticsegmentationmattetypes.md)
  An array of semantic segmentation matte types that the photo render pipeline can deliver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/embedssemanticsegmentationmattesinphoto)*