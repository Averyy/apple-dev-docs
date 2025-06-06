# CKDBRecordFieldLocationListValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the field of type location list.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldLocationListValue {
	string type;
	CKDBLocation[]? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldLocationListValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldlocationlistvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldlocationlistvalue/value.md)
  An array of values, each containing a location coordinates.

## See Also

- [CKDBRecordFieldLocationValue](ckdbrecordfieldlocationvalue.md)
  The value of the field of type location.
- [CKDBRecordFieldEncryptedLocationValue](ckdbrecordfieldencryptedlocationvalue.md)
  The value of the encrypted field of type location.
- [CKDBRecordFieldEncryptedLocationListValue](ckdbrecordfieldencryptedlocationlistvalue.md)
  The value of the encrypted field of type location list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldlocationlistvalue)*