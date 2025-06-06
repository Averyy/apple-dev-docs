# NSDataAsset

**Framework**: UIKit  
**Kind**: class

An object from a data set type stored in an asset catalog.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSDataAsset
```

#### Overview

The object’s content is stored as a set of one or more files with associated device attributes. These sets can also be tagged for use as on-demand resources.

##### Initialize Data Assets

Data assets are initialized from a named data set in an asset catalog. You create data sets during app development. Each data set contains one or more data files. Each file has associated attributes for features of the device, including the minimum amount of memory and the version of Metal. When you initialize the data asset, the system selects the data file that best matches the current device.

For more information on the data set type in an asset catalog, see [`Data Set Type`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/DataSetType.html#//apple_ref/doc/uid/TP40015170-CH23) in [`Asset Catalog Format Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/index.html#//apple_ref/doc/uid/TP40015170). For information on asset catalogs, see [`Managing assets with asset catalogs`](https://developer.apple.com/documentation/Xcode/managing-assets-with-asset-catalogs).

##### Access the Data

You access the data file by using the [`data`](nsdataasset/data.md) property. Because the property is of type [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) it provides methods for accessing the raw data only as bytes and ranges of bytes.

To access structured data, convert the bytes into the appropriate format. The system can convert some data types for you. One example is XML data using the [`init(data:)`](https://developer.apple.com/documentation/foundation/xmlparser/1418103-init) method of [`XMLParser`](https://developer.apple.com/documentation/Foundation/XMLParser). Other data types require code for parsing and converting the raw data. You may need to convert larger data files incrementally.

## Topics

### Initializing the data asset
- [convenience init?(name: NSDataAssetName)](nsdataasset/init(name:).md)
  Initializes and returns an object with a reference to the named data asset in an asset catalog.
- [init?(name: NSDataAssetName, bundle: Bundle)](nsdataasset/init(name:bundle:).md)
  Initializes and returns an object with a reference to the named data asset that’s in an asset catalog in the specified bundle.
### Accessing data
- [var data: Data](nsdataasset/data.md)
  The raw data values in the data asset.
### Getting data asset information
- [var name: NSDataAssetName](nsdataasset/name.md)
  The name of the data set in the asset catalog.
- [typealias NSDataAssetName](nsdataassetname.md)
  The name of a data asset.
- [var typeIdentifier: String](nsdataasset/typeidentifier.md)
  The uniform type identifier for the data asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIImageAsset](uiimageasset.md)
  A container for a collection of images that represent multiple ways of describing a single piece of artwork.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdataasset)*