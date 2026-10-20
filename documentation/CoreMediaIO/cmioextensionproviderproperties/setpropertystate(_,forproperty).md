# setPropertyState(_:forProperty:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Sets a state value for the specified property.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func setPropertyState(_ propertyState: CMIOExtensionPropertyState<AnyObject>?, forProperty property: CMIOExtensionProperty)
```

```objc
- (void) setPropertyState:(CMIOExtensionPropertyState *) propertyState forProperty:(CMIOExtensionProperty) property;
```

#### Discussion

Setting a `nil` property state value doesn’t remove the property.

## Parameters

- `propertyState`: The updated property state.
- `property`: The property to update.

## See Also

### Managing Properties
- [var name: String?](./name.md)
  The provider name.
- [var manufacturer: String?](./manufacturer.md)
  The provider manufacturer.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](./propertiesdictionary.md)
  A dictionary of properties for a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/setpropertystate(_:forproperty:))*