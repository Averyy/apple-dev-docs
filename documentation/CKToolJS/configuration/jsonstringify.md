# jsonStringify

**Framework**: CKTool JS  
**Kind**: property

A function that a request function uses to prepare JSON to send to the API server.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
attribute Function jsonStringify;
```

#### Discussion

The API server can receive numbers larger than the default JavaScript JSON stringify function can handle, so this function is expected to handle large numbers.

This value is only set when `Configuration` is constructed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/configuration/jsonstringify)*