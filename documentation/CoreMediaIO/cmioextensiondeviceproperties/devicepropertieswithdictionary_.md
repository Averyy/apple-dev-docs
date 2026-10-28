# devicePropertiesWithDictionary:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new properties object with a dictionary of property states.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) devicePropertiesWithDictionary:(NSDictionary<NSString *,CMIOExtensionPropertyState *> *) propertiesDictionary;
```

## Return Value

A device properties object.

## Parameters

- `propertiesDictionary`: The dictionary of properties and their states.

## See Also

### Creating Device Properties
- [init(dictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](./init%28dictionary%29.md)
  Creates a properties object with a dictionary of property states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondeviceproperties/devicepropertieswithdictionary:)*