# ALAssetsGroup

**Framework**: Assets Library  
**Kind**: class  
**Role**: Class

An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.

## Declaration

```objc
@interface ALAssetsGroup : NSObject
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`.
>
> In the Photos framework, the [`PHCollection`](../Photos/phcollection.md) and [`PHCollectionList`](../Photos/phcollectionlist.md) classes and their subclasses provide functionality for working with collections of assets.

Assets groups themselves are synced via iTunes, created to hold the user’s saved photos or created during camera import. You can indirectly modify the Saved Photos group by saving images or videos into it using the [`ALAssetsLibrary`](./alassetslibrary.md) class.

## Topics

### Constants
- [ALAssetsGroupEnumerationResultsBlock](./alassetsgroupenumerationresultsblock.md)
  Signature for the block executed during enumeration of assets.
- [Group Property Names](./group-property-names.md)
  Constants for the names of group properties, used by `ALAssetsGroup/value(forProperty:)`.
### Instance Properties
- [editable](./alassetsgroup/editable.md)
### Instance Methods
- [- addAsset:](./alassetsgroup/addasset_.md)
- [- enumerateAssetsAtIndexes:options:usingBlock:](./alassetsgroup/enumerateassetsatindexes_options_usingblock_.md)
- [- enumerateAssetsUsingBlock:](./alassetsgroup/enumerateassetsusingblock_.md)
- [- enumerateAssetsWithOptions:usingBlock:](./alassetsgroup/enumerateassetswithoptions_usingblock_.md)
- [- numberOfAssets](./alassetsgroup/numberofassets.md)
- [- posterImage](./alassetsgroup/posterimage.md)
- [- setAssetsFilter:](./alassetsgroup/setassetsfilter_.md)
- [- valueForProperty:](./alassetsgroup/valueforproperty_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Classes
- [ALAsset](./alasset.md)
  An `ALAsset` object represents a photo or a video managed by the Photo application.
- [ALAssetRepresentation](./alassetrepresentation.md)
  An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](./alasset.md) object.
- [ALAssetsFilter](./alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [ALAssetsLibrary](./alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroup)*