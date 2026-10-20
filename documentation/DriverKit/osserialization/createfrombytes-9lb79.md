# createFromBytes

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static OSSerializationPtr createFromBytes(const void *bytes, size_t length, OSSerializationFreeBufferHandler freeBuffer);
```

#### Discussion

Similar to the above variant, except assuming copyInHandler to be NULL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osserialization/createfrombytes-9lb79)*