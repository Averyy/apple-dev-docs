# propertyStateWithValue:attributes:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new property state with a value and attributes.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) propertyStateWithValue:(ObjectType) value attributes:(CMIOExtensionPropertyAttributes<id> *) attributes;
```

## Return Value

A new property state.

## Parameters

- `value`: The value to associate with the property state.
- `attributes`: The attributes for the property state.

## See Also

### Creating a Property State
- [+ propertyStateWithValue:](./propertystatewithvalue_.md)
  Returns a new property state with a value.
- [convenience init(value: ObjectType?)](./init%28value%29.md)
  Creates a property state with a value.
- [init(value: ObjectType?, attributes: CMIOExtensionPropertyAttributes<ObjectType>?)](./init%28value,attributes%29.md)
  Creates a property state with a value and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertystate/propertystatewithvalue:attributes:)*