# setPropertyState(_:forProperty:)

**Framework**: Core Media I/O  
**Kind**: method

Sets a state value for the specified property.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func setPropertyState(_ propertyState: CMIOExtensionPropertyState<AnyObject>?, forProperty property: CMIOExtensionProperty)
```

#### Discussion

Setting a `nil` property state value doesn’t remove the property.

## Parameters

- `propertyState`: The updated property state.
- `property`: The property to update.

## See Also

- [var name: String?](cmioextensionproviderproperties/name.md)
  The provider name.
- [var manufacturer: String?](cmioextensionproviderproperties/manufacturer.md)
  The provider manufacturer.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](cmioextensionproviderproperties/propertiesdictionary.md)
  A dictionary of properties for a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/setpropertystate(_:forproperty:))*