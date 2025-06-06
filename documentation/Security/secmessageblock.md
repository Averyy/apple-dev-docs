# SecMessageBlock

**Framework**: Security  
**Kind**: typealias

A block that delivers messages during asynchronous operations.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SecMessageBlock = (CFTypeRef?, CFError?, Bool) -> Void
```

## Parameters

- `message`: A CFType containing the message. This is where either intermediate or final results are returned.
- `error`: If an error occurred, this will contain a CFErrorRef, otherwise this will be NULL. If not NULL the caller is responsible for releasing the CFErrorRef.
- `isFinal`: If set the message returned is the final result otherwise it is an intermediate result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secmessageblock)*