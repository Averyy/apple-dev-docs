# CKDBRecordFieldAssetListValue

**Framework**: CKTool JS  
**Kind**: struct

A field value that contains an array of assets.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
dictionary CKDBRecordFieldAssetListValue {
	string type;
	CKDBAsset[]? value;
};
```

#### Overview

In JavaScript, this is a plain object with properties as described.

In TypeScript, this type is imported in the following way:

```javascript
import type { CKDBRecordFieldAssetListValue } from "@apple/cktool.database";
```

## Topics

### Instance Properties
- [type](ckdbrecordfieldassetlistvalue/type.md)
  A string used to identify the field type.
- [value](ckdbrecordfieldassetlistvalue/value.md)
  The array of asset objects in this record field.

## See Also

- [CKDBRecordFieldAssetValue](ckdbrecordfieldassetvalue.md)
  The value of the field of the type asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecordfieldassetlistvalue)*