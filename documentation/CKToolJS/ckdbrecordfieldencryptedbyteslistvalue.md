# CKDBRecordFieldEncryptedBytesListValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the encrypted field of type bytes list.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldEncryptedBytesListValue {
	string type;
	ByteArray[]? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldEncryptedBytesListValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldencryptedbyteslistvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldencryptedbyteslistvalue/value.md)
  An array of strings, each containing a sequence of bytes.

## See Also

- [CKDBRecordFieldBytesValue](ckdbrecordfieldbytesvalue.md)
  A field value that contains an array of bytes.
- [CKDBRecordFieldBytesListValue](ckdbrecordfieldbyteslistvalue.md)
  A field value that contains an array of bytes.
- [CKDBRecordFieldEncryptedBytesValue](ckdbrecordfieldencryptedbytesvalue.md)
  The value of the encrypted field of type bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldencryptedbyteslistvalue)*