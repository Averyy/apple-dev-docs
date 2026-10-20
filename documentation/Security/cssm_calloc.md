# CSSM_CALLOC

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias CSSM_CALLOC = (uint32, CSSM_SIZE, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?
```

```c
typedef void *(*)(unsigned int, unsigned long, void *) CSSM_CALLOC;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_calloc)*