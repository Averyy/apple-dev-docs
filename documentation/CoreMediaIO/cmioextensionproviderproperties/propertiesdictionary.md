# propertiesDictionary

**Framework**: Core Media I/O  
**Kind**: property

A dictionary of properties for a provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>] { get set }
```

## See Also

- [var name: String?](cmioextensionproviderproperties/name.md)
  The provider name.
- [var manufacturer: String?](cmioextensionproviderproperties/manufacturer.md)
  The provider manufacturer.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](cmioextensionproviderproperties/setpropertystate(_:forproperty:).md)
  Sets a state value for the specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/propertiesdictionary)*