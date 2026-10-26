# init(value:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates a property state with a value.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
convenience init(value: ObjectType?)
```

```objc
- (instancetype) initWithValue:(ObjectType) value;
```

#### Discussion

The system supports the following value types: [`NSDictionary`](../../Foundation/nsdictionary.md), [`NSArray`](../../Foundation/nsarray.md), [`NSString`](../../Foundation/nsstring.md), [`NSData`](../../Foundation/nsdata.md), and [`NSNumber`](../../Foundation/nsnumber.md).

## Parameters

- `value`: The value to associate with the property state.

## See Also

### Creating a Property State
- [init(value: ObjectType?, attributes: CMIOExtensionPropertyAttributes<ObjectType>?)](./init%28value,attributes%29.md)
  Creates a property state with a value and attributes.
- [+ propertyStateWithValue:](./propertystatewithvalue_.md)
  Returns a new property state with a value.
- [+ propertyStateWithValue:attributes:](./propertystatewithvalue_attributes_.md)
  Returns a new property state with a value and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertystate/init(value:))*