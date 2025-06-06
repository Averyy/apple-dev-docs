# enabledSemanticSegmentationMatteTypes

**Framework**: AVFoundation  
**Kind**: property

The semantic segmentation matte types that the photo render pipeline delivers.

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

Set this property value to the array of matte types you’d like delivered with your primary photos. The array may only contain values present in [`availableSemanticSegmentationMatteTypes`](avcapturephotooutput/availablesemanticsegmentationmattetypes.md).

The default value of this property is an empty array.

> ❗ **Important**:  Enabling semantic segmentation matte delivery requires a lengthy reconfiguration of the capture render pipeline. If you intend to capture semantic segmentation mattes, set this property to your desired types before calling the capture session’s [`startRunning()`](avcapturesession/startrunning().md) method.

 Enabling semantic segmentation matte delivery requires a lengthy reconfiguration of the capture render pipeline. If you intend to capture semantic segmentation mattes, set this property to your desired types before calling the capture session’s [`startRunning()`](avcapturesession/startrunning().md) method.

## See Also

- [var availableSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType]](avcapturephotooutput/availablesemanticsegmentationmattetypes.md)
  An array of semantic segmentation matte types that may be captured and delivered along with the primary photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/enabledsemanticsegmentationmattetypes)*