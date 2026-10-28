# streamPropertiesWithDictionary:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new properties object that provides the specified properties and default states.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) streamPropertiesWithDictionary:(NSDictionary<NSString *,CMIOExtensionPropertyState *> *) propertiesDictionary;
```

## Return Value

A new stream properties object.

## Parameters

- `propertiesDictionary`: A dictionary of properties and their initial states.

## See Also

### Creating Stream Properties
- [init(dictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](./init%28dictionary%29.md)
  Creates a properties object that provides the specified properties and default states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/streampropertieswithdictionary:)*