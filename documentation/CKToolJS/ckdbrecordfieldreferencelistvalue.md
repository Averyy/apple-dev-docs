# CKDBRecordFieldReferenceListValue

**Framework**: CKTool JS  
**Kind**: struct

The value of the field of type reference list.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldReferenceListValue {
	string type;
	CKDBRecordReference[]? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldReferenceListValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldreferencelistvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldreferencelistvalue/value.md)
  The array of values, each containing a reference to a CloudKit record

## See Also

- [CKDBRecordFieldReferenceValue](ckdbrecordfieldreferencevalue.md)
  The value of the field of type reference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldreferencelistvalue)*