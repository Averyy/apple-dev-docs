# CSSM_MALLOC

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias CSSM_MALLOC = (CSSM_SIZE, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?
```

```c
typedef void *(*)(unsigned long, void *) CSSM_MALLOC;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_malloc)*