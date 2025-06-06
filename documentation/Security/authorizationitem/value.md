# value

**Framework**: Security  
**Kind**: property

A pointer to information pertaining to the name field.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var value: UnsafeMutableRawPointer?
```

#### Discussion

If the `name` field is set to the value represented by the constant [`kAuthorizationRightExecute`](kauthorizationrightexecute.md), then set the `value` field to the full POSIX pathname of the tool you want to execute. In most other cases, set this field to `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationitem/value)*