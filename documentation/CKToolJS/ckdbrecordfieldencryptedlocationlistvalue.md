# CKDBRecordFieldEncryptedLocationListValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the encrypted field of type location list.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldEncryptedLocationListValue {
	string type;
	CKDBLocation[]? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldEncryptedLocationListValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldencryptedlocationlistvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldencryptedlocationlistvalue/value.md)
  An array of location objects.

## See Also

- [CKDBRecordFieldLocationValue](ckdbrecordfieldlocationvalue.md)
  The value of the field of type location.
- [CKDBRecordFieldLocationListValue](ckdbrecordfieldlocationlistvalue.md)
  The value of the field of type location list.
- [CKDBRecordFieldEncryptedLocationValue](ckdbrecordfieldencryptedlocationvalue.md)
  The value of the encrypted field of type location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldencryptedlocationlistvalue)*