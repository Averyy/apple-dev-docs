# setPropertyState(_:forProperty:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Sets the state of the specified property.

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

## Parameters

- `propertyState`: The new state for the property.
- `property`: The property to update.

## See Also

### Managing Property State
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](./propertiesdictionary.md)
  A dictionary representation of the property state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/setpropertystate(_:forproperty:))*