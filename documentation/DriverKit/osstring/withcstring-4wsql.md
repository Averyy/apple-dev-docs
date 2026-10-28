# withCString

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

Allocates an OSString object with a copy of a c-string.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static OSStringPtr withCString(const char *cString);
```

## Return Value

NULL on failure, otherwise the allocated OSString with reference count 1 to be released by the caller.

## Parameters

- `cString`: Pointer to null terminated c-string. The string will be copied at the time of the call.

## See Also

### Creating a String
- [withString](./withstring.md)
  Allocates an OSString object with a copy of an OString object.
- [withCString](./withcstring-721oh.md)
  Allocates an OSString object with a copy of a c-string, up to a given length.
- [withCStringNoCopy](./withcstringnocopy.md)
  Allocates an OSString object with a copy of a c-string.
- [OSStringCreate](../osstringcreate.md)
- [free](./free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring/withcstring-4wsql)*