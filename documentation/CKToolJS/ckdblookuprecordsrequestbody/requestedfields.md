# requestedFields

**Framework**: CKTool JS  
**Kind**: property

The array of record field names that limits the amount of data returned in this operation.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute string[]? requestedFields;
```

#### Discussion

The server only returns the fields specified in the array. If omitted, the server returns all record fields. If set to an empty array, the server returns record metadata without the fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdblookuprecordsrequestbody/requestedfields)*