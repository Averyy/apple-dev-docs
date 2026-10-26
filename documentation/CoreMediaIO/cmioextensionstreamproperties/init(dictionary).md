# init(dictionary:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates a properties object that provides the specified properties and default states.

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

- `propertiesDictionary`: A dictionary of properties and their initial states.

## See Also

### Creating Stream Properties
- [+ streamPropertiesWithDictionary:](./streampropertieswithdictionary_.md)
  Returns a new properties object that provides the specified properties and default states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstreamproperties/init(dictionary:))*