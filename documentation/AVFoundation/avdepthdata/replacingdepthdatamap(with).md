# replacingDepthDataMap(with:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns a derivative depth data object by replacing the depth data map.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func replacingDepthDataMap(with pixelBuffer: CVPixelBuffer) throws -> Self
```

```objc
- (instancetype) depthDataByReplacingDepthDataMapWithPixelBuffer:(CVPixelBufferRef) pixelBuffer error:(NSError **) outError;
```

## Return Value

A new depth data object containing the pixel buffer.

## Discussion

If you apply simple transforms to media containing depth data, you can use the [`applyingExifOrientation(_:)`](./applyingexiforientation%28_%29.md) method to apply parallel transforms to the corresponding depth data. More complex transforms and edits require creating a derivative depth map reflecting whatever edits you make to the corresponding image. In such cases, use this [`replacingDepthDataMap(with:)`](./replacingdepthdatamap%28with%29.md) method to create a derivative depth data object.

> **Note**:  This method cannot ensure correspondence between an arbitrarily edited depth map and the camera parameters that generated the initial depth map, so the new depth data object’s [`cameraCalibrationData`](./cameracalibrationdata.md) property is always `nil`.

## Parameters

- `pixelBuffer`: A pixel buffer containing depth or disparity information in a compatible format.

## See Also

### Transforming and processing
- [func applyingExifOrientation(CGImagePropertyOrientation) -> Self](./applyingexiforientation%28_%29.md)
  Returns a derivative depth data object by mirroring or rotating it to the specified orientation.
- [func converting(toDepthDataType: OSType) -> Self](./converting%28todepthdatatype%29.md)
  Returns a derivative depth data object by converting the depth data map to the specified data type.
- [var availableDepthDataTypes: [OSType]](./availabledepthdatatypes-3ifx1.md)
  The list of depth data formats to which you can convert this depth data.
- [availableDepthDataTypes](./availabledepthdatatypes-472g0.md)
  The list of depth data formats to which you can convert this depth data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/replacingdepthdatamap(with:))*