# providerPropertiesWithDictionary:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new provider properties object with the specified properties.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) providerPropertiesWithDictionary:(NSDictionary<NSString *,CMIOExtensionPropertyState *> *) propertiesDictionary;
```

## Parameters

- `propertiesDictionary`: A dictionary of property states.

## See Also

### Creating Provider Properties
- [init(dictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](./init%28dictionary%29.md)
  Creates a provider properties object with the specified properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties/providerpropertieswithdictionary:)*