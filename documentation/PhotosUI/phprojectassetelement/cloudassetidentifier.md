# cloudAssetIdentifier

**Framework**: PhotosUI  
**Kind**: property  
**Role**: Instance Property

The asset’s identifier in the cloud.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var cloudAssetIdentifier: PHCloudIdentifier { get }
```

```objc
@property (nonatomic, readonly) PHCloudIdentifier * cloudAssetIdentifier;
```

## See Also

### Characterizing an Asset Element
- [var annotation: String](./annotation.md)
  A string annotation attached to the asset.
- [var cropRect: CGRect](./croprect.md)
  A rectangle defining the cropped portion of the asset.
- [var regionsOfInterest: [PHProjectRegionOfInterest]](./regionsofinterest.md)
  An array of regions of interest in the photo asset.
- [var horizontallyFlipped: Bool](./horizontallyflipped.md)
  A Boolean indicating whether the asset is vertically flipped.
- [var verticallyFlipped: Bool](./verticallyflipped.md)
  A Boolean indicating whether the asset is vertically flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectassetelement/cloudassetidentifier)*