# OSObjectAllocate

**Framework**: DriverKit  
**Kind**: func  
**Role**: Function

Helper function for OSTypeAlloc(). Not to be called directly.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
extern kern_return_t OSObjectAllocate(OSMetaClass *meta, OSObject **pObject);
```

## See Also

### Object Support
- [OSObjectRetain](./osobjectretain.md)
- [OSObjectRelease](./osobjectrelease.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osobjectallocate)*