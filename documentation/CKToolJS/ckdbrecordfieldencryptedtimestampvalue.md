# CKDBRecordFieldEncryptedTimestampValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the encrypted field of type timestamp.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldEncryptedTimestampValue {
	string type;
	date? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldEncryptedTimestampValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldencryptedtimestampvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldencryptedtimestampvalue/value.md)
  A string in date-time format.

## See Also

- [CKDBRecordFieldTimestampValue](ckdbrecordfieldtimestampvalue.md)
  The value of the field of type timestamp.
- [CKDBRecordFieldTimestampListValue](ckdbrecordfieldtimestamplistvalue.md)
  The value of the field of type timestamp list.
- [CKDBRecordFieldEncryptedTimestampListValue](ckdbrecordfieldencryptedtimestamplistvalue.md)
  The value of the encrypted field of type timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldencryptedtimestampvalue)*