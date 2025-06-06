# CKDBRecordFieldEncryptedLocationValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the encrypted field of type location.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldEncryptedLocationValue {
	string type;
	CKDBLocation? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldEncryptedLocationValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldencryptedlocationvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldencryptedlocationvalue/value.md)

## See Also

- [CKDBRecordFieldLocationValue](ckdbrecordfieldlocationvalue.md)
  The value of the field of type location.
- [CKDBRecordFieldLocationListValue](ckdbrecordfieldlocationlistvalue.md)
  The value of the field of type location list.
- [CKDBRecordFieldEncryptedLocationListValue](ckdbrecordfieldencryptedlocationlistvalue.md)
  The value of the encrypted field of type location list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldencryptedlocationvalue)*