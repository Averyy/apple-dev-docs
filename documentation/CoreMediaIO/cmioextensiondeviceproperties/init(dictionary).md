# init(dictionary:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates a properties object with a dictionary of property states.

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

- `propertiesDictionary`: The dictionary of properties and their states.

## See Also

### Creating Device Properties
- [+ devicePropertiesWithDictionary:](./devicepropertieswithdictionary_.md)
  Returns a new properties object with a dictionary of property states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties/init(dictionary:))*