# AuthorizationString

**Framework**: Security  
**Kind**: typealias

A zero-terminated string in UTF-8 encoding.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias AuthorizationString = UnsafePointer<CChar>
```

#### Discussion

Use this in a call to the [`AuthorizationCopyInfo(_:_:_:)`](authorizationcopyinfo(_:_:_:).md) function for the `tag` parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationstring)*