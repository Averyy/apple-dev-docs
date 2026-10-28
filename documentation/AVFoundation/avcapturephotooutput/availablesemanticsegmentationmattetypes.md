# availableSemanticSegmentationMatteTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of semantic segmentation matte types that may be captured and delivered along with the primary photo.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var availableSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableSemanticSegmentationMatteTypes;
```

## Discussion

This property returns the array of semantic segmentation types that’s available given the current session configuration.

This property is key-value observable.

> ❗ **Important**:  The value of this property may change when switching cameras or formats. When this property changes, [`enabledSemanticSegmentationMatteTypes`](./enabledsemanticsegmentationmattetypes.md) reverts to an empty array. If you’ve previously opted in for delivery of one or more semantic segmentation mattes, you need to set up your [`enabledSemanticSegmentationMatteTypes`](./enabledsemanticsegmentationmattetypes.md) again.

## See Also

### Getting segmentation mattes
- [var enabledSemanticSegmentationMatteTypes: [AVSemanticSegmentationMatte.MatteType]](./enabledsemanticsegmentationmattetypes.md)
  The semantic segmentation matte types that the photo render pipeline delivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablesemanticsegmentationmattetypes)*