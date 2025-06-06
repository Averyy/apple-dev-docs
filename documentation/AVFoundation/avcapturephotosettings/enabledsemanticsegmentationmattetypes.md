# enabledSemanticSegmentationMatteTypes

**Framework**: AVFoundation  
**Kind**: property

An array of semantic segmentation matte types that the photo render pipeline can deliver.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var enabledSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType] { get set }
```

#### Discussion

You may set this property to the array of matte types you’d like delivered with [`AVCapturePhoto`](avcapturephoto.md). The array may only contain values present in [`availableSemanticSegmentationMatteTypes`](avcapturephotooutput/availablesemanticsegmentationmattetypes.md).

The default value of this property is an empty array.

## See Also

- [var embedsSemanticSegmentationMattesInPhoto: Bool](avcapturephotosettings/embedssemanticsegmentationmattesinphoto.md)
  A Boolean value that specifies whether to write the enabled semantic segmentation matte types captured with this photo to the photo’s file structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/enabledsemanticsegmentationmattetypes)*