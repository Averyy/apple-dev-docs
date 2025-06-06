# recordChangeTag

**Framework**: CKTool JS  
**Kind**: property

A string containing the server change token for the record.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute string? recordChangeTag;
```

#### Discussion

Use this tag to indicate which version of the record you last fetched. This tag is required unless force parameter for updateRecord operation is set to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/ckdbmodifyrecordrequestbody/recordchangetag)*