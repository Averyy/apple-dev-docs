# getCStringNoCopy

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a pointer to the OSString object’s internal data buffer.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
const char * getCStringNoCopy() const;
```

#### Return Value

A pointer to the string or NULL if the OSString has zero length. The string will be null terminated.

## See Also

### Getting a C String
- [OSStringGetStringPtr](../osstringgetstringptr.md)
- [OSStringPtr](../osstringptr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring/getcstringnocopy)*