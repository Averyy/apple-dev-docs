# init(name:)

**Framework**: UIKit  
**Kind**: init

Initializes and returns an object with a reference to the named data asset in an asset catalog.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init?(name: NSDataAssetName)
```

#### Return Value

The data asset object for the named data set, or `nil` if the data set is not found.

#### Discussion

If there are multiple data files in the named data set, this method returns the one with attributes that most closely match the current device available screen space.

This method looks in the asset catalog, in the main bundle for the named data set.

## Parameters

- `name`: The name of the data set in the asset catalog.

## See Also

- [init?(name: NSDataAssetName, bundle: Bundle)](nsdataasset/init(name:bundle:).md)
  Initializes and returns an object with a reference to the named data asset that’s in an asset catalog in the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdataasset/init(name:))*