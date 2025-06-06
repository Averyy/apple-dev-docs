# label

**Framework**: Contacts  
**Kind**: property

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

#### Discussion

Labeled property is used only for properties that are in labeled arrays. If the property is not an array of labeled values, the value of the label is `nil`.

## See Also

- [var key: String](cncontactproperty/key.md)
  The key of the contact property.
- [var value: Any?](cncontactproperty/value.md)
  The value of the property.
- [var identifier: String?](cncontactproperty/identifier.md)
  The identifier of the labeled value in the array of labeled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactproperty/label)*