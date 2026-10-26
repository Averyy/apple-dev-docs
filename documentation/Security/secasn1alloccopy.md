# SecAsn1AllocCopy

**Framework**: Security  
**Kind**: func  
**Role**: Function

Allocates memory for an item’s data field in the coder object’s memory pool and copies in a block of data.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecAsn1AllocCopy(SecAsn1CoderRef coder, const void *src, size_t len, SecAsn1Item *dest);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secasn1alloccopy)*