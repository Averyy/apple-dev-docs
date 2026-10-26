# init(dictionary:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates a provider properties object with the specified properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(dictionary propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])
```

```objc
- (instancetype) initWithDictionary:(NSDictionary<NSString *,CMIOExtensionPropertyState *> *) propertiesDictionary;
```

## Parameters

- `propertiesDictionary`: A dictionary of property states.

## See Also

### Creating Provider Properties
- [+ providerPropertiesWithDictionary:](./providerpropertieswithdictionary_.md)
  Returns a new provider properties object with the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/init(dictionary:))*