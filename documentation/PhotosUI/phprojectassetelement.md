# PHProjectAssetElement

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

An element that represents a media asset within project section content.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class PHProjectAssetElement
```

```objc
@interface PHProjectAssetElement : PHProjectElement
```

## Overview

Access the underlying [`PHAsset`](../Photos/phasset.md) by converting the provided [`cloudAssetIdentifiers`](./phprojectsectioncontent/cloudassetidentifiers.md) to a [`assetLocalIdentifier`](../Photos/phassetresource/assetlocalidentifier.md), then calling [`fetchAssets(withLocalIdentifiers:options:)`](../Photos/phasset/fetchassets%28withlocalidentifiers,options%29.md).

## Topics

### Characterizing an Asset Element
- [var annotation: String](./phprojectassetelement/annotation.md)
  A string annotation attached to the asset.
- [var cloudAssetIdentifier: PHCloudIdentifier](./phprojectassetelement/cloudassetidentifier.md)
  The asset’s identifier in the cloud.
- [var cropRect: CGRect](./phprojectassetelement/croprect.md)
  A rectangle defining the cropped portion of the asset.
- [var regionsOfInterest: [PHProjectRegionOfInterest]](./phprojectassetelement/regionsofinterest.md)
  An array of regions of interest in the photo asset.
- [var horizontallyFlipped: Bool](./phprojectassetelement/horizontallyflipped.md)
  A Boolean indicating whether the asset is vertically flipped.
- [var verticallyFlipped: Bool](./phprojectassetelement/verticallyflipped.md)
  A Boolean indicating whether the asset is vertically flipped.

## Relationships

### Inherits From
- [PHProjectElement](./phprojectelement.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Subclassing Project Elements
- [class PHProjectTextElement](./phprojecttextelement.md)
  An element that represents text within project section content.
- [class PHProjectJournalEntryElement](./phprojectjournalentryelement.md)
  An element that represents a journal entry within project section content.
- [class PHProjectMapElement](./phprojectmapelement.md)
  An element that represents a map within project section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectassetelement)*