# init(value:)

**Framework**: Core Media I/O  
**Kind**: init

Creates a property state with a value.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
convenience init(value: ObjectType?)
```

#### Discussion

The system supports the following value types: [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary), [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray), [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSData`](https://developer.apple.com/documentation/Foundation/NSData), and [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).

## Parameters

- `value`: The value to associate with the property state.

## See Also

- [init(value: ObjectType?, attributes: CMIOExtensionPropertyAttributes<ObjectType>?)](cmioextensionpropertystate/init(value:attributes:).md)
  Creates a property state with a value and attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionpropertystate/init(value:))*