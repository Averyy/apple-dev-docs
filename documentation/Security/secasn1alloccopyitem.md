# SecAsn1AllocCopyItem

**Framework**: Security  
**Kind**: func  
**Role**: Function

Allocates memory for an item’s data field in the coder object’s memory pool and copies in a block of data from another item.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

## Declaration

```c
OSStatus SecAsn1AllocCopyItem(SecAsn1CoderRef coder, const SecAsn1Item *src, SecAsn1Item *dest);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secasn1alloccopyitem)*