# propertiesDictionary

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

A dictionary of properties for a provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>] { get set }
```

```objc
@property (atomic, copy) NSDictionary<NSString *,CMIOExtensionPropertyState *> * propertiesDictionary;
```

## See Also

### Managing Properties
- [var name: String?](./name.md)
  The provider name.
- [var manufacturer: String?](./manufacturer.md)
  The provider manufacturer.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](./setpropertystate%28_,forproperty%29.md)
  Sets a state value for the specified property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/propertiesdictionary)*