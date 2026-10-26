# quality

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The region’s quality.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var quality: Double { get }
```

```objc
@property (nonatomic, readonly) double quality;
```

#### Discussion

The `quality` score represents the quality of the region of interest in the individual asset, based on factors like sharpness, visibility, and prominence in the photo. Values range from `0` to `1`, with a default of `0.5`. Different regions of interest with the same identifier may have different quality values. If a project must choose between multiple assets containing the same region of interest, use the `quality` metric to choose the best representative.

![Two photos containing the same human faces, one with low quality, the other with high quality](https://developer.apple.com/tutorials/images/com.apple.photokit/media-3030183@2x.png)

## See Also

### Determining Region Properties
- [var rect: CGRect](./rect.md)
  The rectangle representing the region’s location.
- [var identifier: PHProjectRegionOfInterest.Identifier](./identifier-swift.property.md)
  The region’s unique identifier.
- [var weight: Double](./weight.md)
  The face region’s weight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectregionofinterest/quality)*