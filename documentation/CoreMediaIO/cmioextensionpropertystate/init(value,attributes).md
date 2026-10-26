# init(value:attributes:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates a property state with a value and attributes.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(value: ObjectType?, attributes: CMIOExtensionPropertyAttributes<ObjectType>?)
```

```objc
- (instancetype) initWithValue:(ObjectType) value attributes:(CMIOExtensionPropertyAttributes<id> *) attributes;
```

## Parameters

- `value`: The value to associate with the property state.
- `attributes`: The attributes for the property state.

## See Also

### Creating a Property State
- [convenience init(value: ObjectType?)](./init%28value%29.md)
  Creates a property state with a value.
- [+ propertyStateWithValue:](./propertystatewithvalue_.md)
  Returns a new property state with a value.
- [+ propertyStateWithValue:attributes:](./propertystatewithvalue_attributes_.md)
  Returns a new property state with a value and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertystate/init(value:attributes:))*