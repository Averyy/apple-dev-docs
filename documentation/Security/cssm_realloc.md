# CSSM_REALLOC

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias CSSM_REALLOC = (UnsafeMutableRawPointer?, CSSM_SIZE, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?
```

```c
typedef void *(*)(void *, unsigned long, void *) CSSM_REALLOC;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_realloc)*