# value(forProperty:)

**Framework**: Assets Library  
**Kind**: method

Returns the value for a given property.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func value(forProperty property: String!) -> Any!
```

#### Return Value

The value for `property`. If `property` is not a valid key, returns [`ALErrorInvalidProperty`](alerrorinvalidproperty.md).

## Parameters

- `property`: The property for which you want the value. For valid keys, see  .

## See Also

- [var isEditable: Bool](alasset/iseditable.md)
  Indicates whether the asset is editable.
- [var original: ALAsset!](alasset/original.md)
  The original version of the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alasset/value(forproperty:))*