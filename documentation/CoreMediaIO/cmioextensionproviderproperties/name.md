# name

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

The provider name.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (atomic, strong, nullable) NSString * name;
```

#### Discussion

The key for this property is [`providerName`](../cmioextensionproperty/providername.md).

## See Also

### Managing Properties
- [var manufacturer: String?](./manufacturer.md)
  The provider manufacturer.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](./setpropertystate%28_,forproperty%29.md)
  Sets a state value for the specified property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](./propertiesdictionary.md)
  A dictionary of properties for a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/name)*