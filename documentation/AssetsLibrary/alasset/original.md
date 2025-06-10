# original

**Framework**: Assets Library  
**Kind**: property

The original version of the asset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var original: ALAsset! { get }
```

#### Discussion

The property value is the original asset if the receiver was saved as a modified version of an asset. The property value is `nil` if the asset was not saved as a modified version of another asset.

## See Also

- [func value(forProperty: String!) -> Any!](alasset/value(forproperty:).md)
  Returns the value for a given property.
- [var isEditable: Bool](alasset/iseditable.md)
  Indicates whether the asset is editable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/original)*