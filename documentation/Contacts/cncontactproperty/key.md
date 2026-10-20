# key

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The key of the contact property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var key: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * key;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * key;
```

#### Discussion

This property is used for properties that may or may not be in labeled arrays.

## See Also

### Getting the Property Information
- [var value: Any?](./value.md)
  The value of the property.
- [var label: String?](./label.md)
  The label of the labeled value of the property array.
- [var identifier: String?](./identifier.md)
  The identifier of the labeled value in the array of labeled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactproperty/key)*