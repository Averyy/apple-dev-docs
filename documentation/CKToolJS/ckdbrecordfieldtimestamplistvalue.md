# CKDBRecordFieldTimestampListValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the field of type timestamp list.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldTimestampListValue {
	string type;
	Date[]? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldTimestampListValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldtimestamplistvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldtimestamplistvalue/value.md)
  An array of strings in date-time format.

## See Also

- [CKDBRecordFieldTimestampValue](ckdbrecordfieldtimestampvalue.md)
  The value of the field of type timestamp.
- [CKDBRecordFieldEncryptedTimestampValue](ckdbrecordfieldencryptedtimestampvalue.md)
  The value of the encrypted field of type timestamp.
- [CKDBRecordFieldEncryptedTimestampListValue](ckdbrecordfieldencryptedtimestamplistvalue.md)
  The value of the encrypted field of type timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldtimestamplistvalue)*