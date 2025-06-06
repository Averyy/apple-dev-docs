# CKDBRecordFieldBytesListValue

**Framework**: CKTool JS  
**Kind**: struct

A field value that contains an array of bytes.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldBytesListValue {
	string type;
	ByteArray[]? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldBytesListValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldbyteslistvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldbyteslistvalue/value.md)
  A field value that contains an array of byte arrays.

## See Also

- [CKDBRecordFieldBytesValue](ckdbrecordfieldbytesvalue.md)
  A field value that contains an array of bytes.
- [CKDBRecordFieldEncryptedBytesValue](ckdbrecordfieldencryptedbytesvalue.md)
  The value of the encrypted field of type bytes.
- [CKDBRecordFieldEncryptedBytesListValue](ckdbrecordfieldencryptedbyteslistvalue.md)
  The value of the encrypted field of type bytes list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldbyteslistvalue)*