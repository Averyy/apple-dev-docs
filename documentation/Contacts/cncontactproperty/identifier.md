# identifier

**Framework**: Contacts  
**Kind**: property

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

#### Discussion

Identifier is used only for properties in labeled arrays. If the property is not an array of labeled values, the value of the identifier is `nil`.

## See Also

- [var key: String](cncontactproperty/key.md)
  The key of the contact property.
- [var value: Any?](cncontactproperty/value.md)
  The value of the property.
- [var label: String?](cncontactproperty/label.md)
  The label of the labeled value of the property array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactproperty/identifier)*