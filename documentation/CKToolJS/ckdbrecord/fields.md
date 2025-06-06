# fields

**Framework**: CKTool JS  
**Kind**: property

The dictionary of key-value pairs whose keys are the record field names and values are field-value dictionaries.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute dictionary fields;
```

#### Discussion

Values in this dictionary conform to `CKDBRecordFieldValue`. `CKDBRecordFieldValue` is the root of the hierarchy of valid record field value types, such as `CKDBRecordFieldStringValue`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbrecord/fields)*