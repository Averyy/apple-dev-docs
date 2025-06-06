# jsonParse

**Framework**: CKTool JS  
**Kind**: property

A function that a response parser uses to interpret JSON from the API server.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute Function jsonParse;
```

#### Discussion

The API server can send numbers larger than the default JavaScript JSON parse function can handle, so this function is expected to handle large numbers.

This value is only set when `Configuration` is constructed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/configuration/jsonparse)*