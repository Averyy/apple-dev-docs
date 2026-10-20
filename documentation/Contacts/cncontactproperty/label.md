# label

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The label of the labeled value of the property array.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var label: String? { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * label;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * label;
```

#### Discussion

Labeled property is used only for properties that are in labeled arrays. If the property is not an array of labeled values, the value of the label is `nil`.

## See Also

### Getting the Property Information
- [var key: String](./key.md)
  The key of the contact property.
- [var value: Any?](./value.md)
  The value of the property.
- [var identifier: String?](./identifier.md)
  The identifier of the labeled value in the array of labeled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactproperty/label)*