# value

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The value of the property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var value: Any? { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) id value;
```

*macOS*

```objc
@property (atomic, readonly, nullable) id value;
```

#### Discussion

This property is used for properties that may or may not be in labeled arrays.

## See Also

### Getting the Property Information
- [var key: String](./key.md)
  The key of the contact property.
- [var label: String?](./label.md)
  The label of the labeled value of the property array.
- [var identifier: String?](./identifier.md)
  The identifier of the labeled value in the array of labeled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactproperty/value)*