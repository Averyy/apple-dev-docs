# fieldType

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The type of this editable field.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var fieldType: ASImportableEditableField.FieldType
```

## Discussion

This value must be one of:

- `string`
- `concealed-string`
- `email`
- `number`
- `boolean`
- `date`

## See Also

### Accessing field properties
- [var id: Data?](./id.md)
  A unique identifier for this editable field.
- [ASImportableEditableField.FieldType](./fieldtype-swift.enum.md)
  An enumeration of editable field types.
- [var value: String](./value.md)
  The value stored in this editable field.
- [var label: String?](./label.md)
  A value describing the field, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableeditablefield/fieldtype-swift.property)*