# ASImportableEditableField

**Framework**: Authentication Services  
**Kind**: struct

A field that someone can edit within a credential.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ASImportableEditableField
```

#### Overview

Examples of editable fields include `ASImportableCredential/BasicAuthentication/username` and [`password`](asimportablecredential/basicauthentication/password.md) in [`ASImportableCredential.BasicAuthentication`](asimportablecredential/basicauthentication.md).

This type is a representation of `EditableField` as defined in the Credential Exchange Format (CXF) specification. You can supply a JSON representation of a CXF `EditableField` to initialize an instance of this struct by using a [`JSONDecoder`](https://developer.apple.com/documentation/Foundation/JSONDecoder) and calling [`decode(_:from:)`](https://developer.apple.com/documentation/Foundation/JSONDecoder/decode(_:from:)).

## Topics

### Creating an editable field
- [init(id: Data?, fieldType: ASImportableEditableField.FieldType, value: String, label: String?)](asimportableeditablefield/init(id:fieldtype:value:label:).md)
  Creates an editable field instance.
### Accessing field properties
- [var id: Data?](asimportableeditablefield/id.md)
  A unique identifier for this editable field.
- [var fieldType: ASImportableEditableField.FieldType](asimportableeditablefield/fieldtype-swift.property.md)
  The type of this editable field.
- [ASImportableEditableField.FieldType](asimportableeditablefield/fieldtype-swift.enum.md)
  An enumeration of editable field types.
- [var value: String](asimportableeditablefield/value.md)
  The value stored in this editable field.
- [var label: String?](asimportableeditablefield/label.md)
  A value describing the field, if any.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var password: ASImportableEditableField?](asimportablecredential/basicauthentication/password.md)
  The password associated with the credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportableeditablefield)*