# CKDBRecordFieldTimestampValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the field of type timestamp.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldTimestampValue {
	string type;
	date? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldTimestampValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldtimestampvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldtimestampvalue/value.md)
  A string in date-time format.

## See Also

- [CKDBRecordFieldTimestampListValue](ckdbrecordfieldtimestamplistvalue.md)
  The value of the field of type timestamp list.
- [CKDBRecordFieldEncryptedTimestampValue](ckdbrecordfieldencryptedtimestampvalue.md)
  The value of the encrypted field of type timestamp.
- [CKDBRecordFieldEncryptedTimestampListValue](ckdbrecordfieldencryptedtimestamplistvalue.md)
  The value of the encrypted field of type timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldtimestampvalue)*