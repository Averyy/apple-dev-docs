# identifier

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The identifier of the labeled value in the array of labeled.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var identifier: String? { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * identifier;
```

#### Discussion

Identifier is used only for properties in labeled arrays. If the property is not an array of labeled values, the value of the identifier is `nil`.

## See Also

### Getting the Property Information
- [var key: String](./key.md)
  The key of the contact property.
- [var value: Any?](./value.md)
  The value of the property.
- [var label: String?](./label.md)
  The label of the labeled value of the property array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactproperty/identifier)*