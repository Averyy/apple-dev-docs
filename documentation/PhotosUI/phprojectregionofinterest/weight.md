# weight

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The face region’s weight.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var weight: Double { get }
```

```objc
@property (nonatomic, readonly) double weight;
```

#### Discussion

The `weight` of a region of interest represents the pervasiveness of the face across the project as a whole. All regions of interest with the same identifier share the same weight. The values range between `0` and `1`. The default value is `0.5`.

![Four photos containing five different human faces, each showing up at different frequencies](https://developer.apple.com/tutorials/images/com.apple.photokit/media-3030188@2x.png)

For projects focused on animation or transition between assets, focus on the regions with the highest weight to ensure that your presentation features areas of greatest interest to the user.

## See Also

### Determining Region Properties
- [var rect: CGRect](./rect.md)
  The rectangle representing the region’s location.
- [var identifier: PHProjectRegionOfInterest.Identifier](./identifier-swift.property.md)
  The region’s unique identifier.
- [var quality: Double](./quality.md)
  The region’s quality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectregionofinterest/weight)*