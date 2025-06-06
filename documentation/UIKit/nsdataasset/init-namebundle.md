# init(name:bundle:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns an object with a reference to the named data asset that’s in an asset catalog in the specified bundle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(name: NSDataAssetName, bundle: Bundle)
```

#### Return Value

The data asset object for the named data set in the specified bundle, or `nil` if the data set is not found.

#### Discussion

If there are multiple data files in the named data set, this method returns the one with attributes that most closely match the current device available screen space.

This method looks in the asset catalog, in the bundle specified by the `bundle` parameter for the named data set.

## Parameters

- `name`: The name of the data set in the asset catalog.
- `bundle`: The bundle used to store the asset catalog. Pass   for the main bundle. The bundle must be the same as the one used in the Xcode project.

## See Also

- [convenience init?(name: NSDataAssetName)](nsdataasset/init(name:).md)
  Initializes and returns an object with a reference to the named data asset in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdataasset/init(name:bundle:))*