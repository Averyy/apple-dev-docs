# ALAssetsGroupEnumerationResultsBlock

**Framework**: Assets Library  
**Kind**: typealias

Signature for the block executed during enumeration of assets.

## Declaration

```swift
typealias ALAssetsGroupEnumerationResultsBlock = (ALAsset?, Int, UnsafeMutablePointer<ObjCBool>?) -> Void
```

#### Discussion

The block takes the following arguments:

If no asset is found, index is set to `NSNotFound`.

The value is set to [`true`](https://developer.apple.com/documentation/Swift/true) if no asset is found.

If the application is not given access to the data, `result` is `nil`, `index` is `NSNotFound`, and `stop` points to [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [Group Property Names](group-property-names.md)
  Constants for the names of group properties, used by [`value(forProperty:)`](alassetsgroup/value(forproperty:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetsgroupenumerationresultsblock)*