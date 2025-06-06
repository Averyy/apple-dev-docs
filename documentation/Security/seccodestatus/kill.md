# kill

**Framework**: Security  
**Kind**: property

The code wants to be terminated if it ever loses its validity.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var kill: SecCodeStatus { get }
```

#### Discussion

This bit can not be cleared on running code; it can only be set. Running code that has this flag set is guaranteed to be valid, because if it were invalid it would have been terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodestatus/kill)*