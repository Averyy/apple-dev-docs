# manufacturer

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The provider manufacturer.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var manufacturer: String? { get set }
```

```objc
@property (atomic, strong, nullable) NSString * manufacturer;
```

## Discussion

The key for this property is [`providerManufacturer`](../cmioextensionproperty/providermanufacturer.md).

## See Also

### Managing Properties
- [var name: String?](./name.md)
  The provider name.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](./setpropertystate%28_,forproperty%29.md)
  Sets a state value for the specified property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](./propertiesdictionary.md)
  A dictionary of properties for a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/manufacturer)*