# CKDBRecordFieldBytesValue

**Framework**: CKTool JS  
**Kind**: struct

A field value that contains an array of bytes.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldBytesValue {
	string type;
	ByteArray? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldBytesValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldbytesvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldbytesvalue/value.md)
  The array of bytes this field contains.

## See Also

- [CKDBRecordFieldBytesListValue](ckdbrecordfieldbyteslistvalue.md)
  A field value that contains an array of bytes.
- [CKDBRecordFieldEncryptedBytesValue](ckdbrecordfieldencryptedbytesvalue.md)
  The value of the encrypted field of type bytes.
- [CKDBRecordFieldEncryptedBytesListValue](ckdbrecordfieldencryptedbyteslistvalue.md)
  The value of the encrypted field of type bytes list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldbytesvalue)*