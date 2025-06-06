# cssm_memory_funcs

**Framework**: Security  
**Kind**: struct

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct cssm_memory_funcs
```

## Topics

### Initializers
- [init()](cssm_memory_funcs-swift.struct/init.md)
- [init(malloc_func: CSSM_MALLOC!, free_func: CSSM_FREE!, realloc_func: CSSM_REALLOC!, calloc_func: CSSM_CALLOC!, AllocRef: UnsafeMutableRawPointer!)](cssm_memory_funcs-swift.struct/init(malloc_func:free_func:realloc_func:calloc_func:allocref:).md)
### Instance Properties
- [var AllocRef: UnsafeMutableRawPointer!](cssm_memory_funcs-swift.struct/allocref.md)
- [var calloc_func: CSSM_CALLOC!](cssm_memory_funcs-swift.struct/calloc_func.md)
- [var free_func: CSSM_FREE!](cssm_memory_funcs-swift.struct/free_func.md)
- [var malloc_func: CSSM_MALLOC!](cssm_memory_funcs-swift.struct/malloc_func.md)
- [var realloc_func: CSSM_REALLOC!](cssm_memory_funcs-swift.struct/realloc_func.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_memory_funcs-swift.struct)*