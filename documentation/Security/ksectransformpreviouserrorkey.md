# kSecTransformPreviousErrorKey

**Framework**: Security  
**Kind**: var

The key in an error’s `userInfo` dictionary whose value specifies the previous error when multiple errors occur during transform evaluation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecTransformPreviousErrorKey: CFString
```

#### Discussion

Use the value associated with this key to trace through a chain of [`CFError`](https://developer.apple.com/documentation/corefoundation/cferror) objects when more than one error occurs during transform evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformpreviouserrorkey)*