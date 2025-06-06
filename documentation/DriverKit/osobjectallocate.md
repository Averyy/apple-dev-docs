# OSObjectAllocate

**Framework**: DriverKit  
**Kind**: func

Helper function for OSTypeAlloc(). Not to be called directly.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
extern kern_return_t OSObjectAllocate(OSMetaClass * meta, OSObject * * pObject);
```

## See Also

- [OSObjectRetain](osobjectretain.md)
- [OSObjectRelease](osobjectrelease.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osobjectallocate)*