# CKDBRecordFieldEncryptedTimestampListValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the encrypted field of type timestamp.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldEncryptedTimestampListValue {
	string type;
	Date[]? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldEncryptedTimestampListValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldencryptedtimestamplistvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldencryptedtimestamplistvalue/value.md)
  An array of strings in date-time format.

## See Also

- [CKDBRecordFieldTimestampValue](ckdbrecordfieldtimestampvalue.md)
  The value of the field of type timestamp.
- [CKDBRecordFieldTimestampListValue](ckdbrecordfieldtimestamplistvalue.md)
  The value of the field of type timestamp list.
- [CKDBRecordFieldEncryptedTimestampValue](ckdbrecordfieldencryptedtimestampvalue.md)
  The value of the encrypted field of type timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldencryptedtimestamplistvalue)*