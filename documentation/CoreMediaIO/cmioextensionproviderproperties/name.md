# name

**Framework**: Core Media I/O  
**Kind**: property

The provider name.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var name: String? { get set }
```

#### Discussion

The key for this property is [`providerName`](cmioextensionproperty/providername.md).

## See Also

- [var manufacturer: String?](cmioextensionproviderproperties/manufacturer.md)
  The provider manufacturer.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](cmioextensionproviderproperties/setpropertystate(_:forproperty:).md)
  Sets a state value for the specified property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](cmioextensionproviderproperties/propertiesdictionary.md)
  A dictionary of properties for a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/name)*