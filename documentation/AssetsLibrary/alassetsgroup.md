# ALAssetsGroup

**Framework**: Assets Library  
**Kind**: class

An `ALAssetsGroup` object represents an ordered set of the assets managed by the Photos application. The order of the elements is the same as the user sees in the Photos application. An asset can belong to multiple assets groups.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class ALAssetsGroup
```

#### Overview

> ❗ **Important**:  The Assets Library framework is deprecated as of iOS 9.0. Instead, use the Photos framework instead, which in iOS 8.0 and later provides more features and better performance for working with a user’s photo library. For more information, see `Photos`. In the Photos framework, the [`PHCollection`](https://developer.apple.com/documentation/Photos/PHCollection) and [`PHCollectionList`](https://developer.apple.com/documentation/Photos/PHCollectionList) classes and their subclasses provide functionality for working with collections of assets.

Assets groups themselves are synced via iTunes, created to hold the user’s saved photos or created during camera import. You can indirectly modify the Saved Photos group by saving images or videos into it using the [`ALAssetsLibrary`](alassetslibrary.md) class.

## Topics

### Enumerating Assets
- [func enumerateAssets(ALAssetsGroupEnumerationResultsBlock!)](alassetsgroup/enumerateassets(_:).md)
  Invokes a given block using each of the assets in the group.
- [func enumerateAssets(options: NSEnumerationOptions, using: ALAssetsGroupEnumerationResultsBlock!)](alassetsgroup/enumerateassets(options:using:).md)
  Invokes a given block using each of the assets in the group.
- [func enumerateAssets(at: IndexSet!, options: NSEnumerationOptions, using: ALAssetsGroupEnumerationResultsBlock!)](alassetsgroup/enumerateassets(at:options:using:).md)
  Invokes a given block using each of the assets in the group at specified indexes.
### Adding Assets
- [func add(ALAsset!) -> Bool](alassetsgroup/add(_:).md)
  Adds an existing asset to the receiver.
- [var isEditable: Bool](alassetsgroup/iseditable.md)
  Indicates whether the application can edit the group.
### Filtering
- [func numberOfAssets() -> Int](alassetsgroup/numberofassets.md)
  Returns the number of assets in the group that match the current filter.
- [func setAssetsFilter(ALAssetsFilter!)](alassetsgroup/setassetsfilter(_:).md)
  Sets the filter for the group.
### Accessing Properties
- [func value(forProperty: String!) -> Any!](alassetsgroup/value(forproperty:).md)
  Returns the group’s value for a given property.
- [func posterImage() -> Unmanaged<CGImage>!](alassetsgroup/posterimage.md)
  Returns the group’s poster image
### Constants
- [typealias ALAssetsGroupEnumerationResultsBlock](alassetsgroupenumerationresultsblock.md)
  Signature for the block executed during enumeration of assets.
- [Group Property Names](group-property-names.md)
  Constants for the names of group properties, used by [`value(forProperty:)`](alassetsgroup/value(forproperty:).md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ALAsset](alasset.md)
  An `ALAsset` object represents a photo or a video managed by the Photo application.
- [class ALAssetRepresentation](alassetrepresentation.md)
  An `ALAssetRepresentation` object encapsulates one of the representations of a given [`ALAsset`](alasset.md) object.
- [class ALAssetsFilter](alassetsfilter.md)
  `ALAssetsFilter` encapsulates filtering criteria to be used when retrieving assets from a group.
- [class ALAssetsLibrary](alassetslibrary.md)
  An instance of `ALAssetsLibrary` provides access to the videos and photos that are under the control of the Photos application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroup)*