# ASImportableEditableField.FieldType

**Framework**: Authentication Services  
**Kind**: enum  
**Role**: Enumeration

An enumeration of editable field types.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum FieldType
```

## Topics

### Determining field type
- [ASImportableEditableField.FieldType.boolean](./fieldtype-swift.enum/boolean.md)
  A type for a Boolean value field.
- [ASImportableEditableField.FieldType.concealedString](./fieldtype-swift.enum/concealedstring.md)
  A type for a concealed string field.
- [ASImportableEditableField.FieldType.date](./fieldtype-swift.enum/date.md)
  A type for a date field.
- [ASImportableEditableField.FieldType.email](./fieldtype-swift.enum/email.md)
  A type for an email field.
- [ASImportableEditableField.FieldType.number](./fieldtype-swift.enum/number.md)
  A type for a number field.
- [ASImportableEditableField.FieldType.string](./fieldtype-swift.enum/string.md)
  A type for a concealed string field.
### Enumeration Cases
- [ASImportableEditableField.FieldType.countryCode](./fieldtype-swift.enum/countrycode.md)
- [ASImportableEditableField.FieldType.subdivisionCode](./fieldtype-swift.enum/subdivisioncode.md)
- [ASImportableEditableField.FieldType.wifiNetworkSecurityType](./fieldtype-swift.enum/wifinetworksecuritytype.md)
- [ASImportableEditableField.FieldType.yearMonth](./fieldtype-swift.enum/yearmonth.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing field properties
- [var id: Data?](./id.md)
  A unique identifier for this editable field.
- [var fieldType: ASImportableEditableField.FieldType](./fieldtype-swift.property.md)
  The type of this editable field.
- [var value: String](./value.md)
  The value stored in this editable field.
- [var label: String?](./label.md)
  A value describing the field, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableeditablefield/fieldtype-swift.enum)*