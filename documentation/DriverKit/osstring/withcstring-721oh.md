# withCString

**Framework**: DriverKit  
**Kind**: method  
**Role**: Static Method

Allocates an OSString object with a copy of a c-string, up to a given length.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
static OSStringPtr withCString(const char *cString, size_t length);
```

## Return Value

NULL on failure, otherwise the allocated OSString with reference count 1 to be released by the caller.

## Parameters

- `cString`: Pointer to null terminated c-string. The string will be copied at the time of the call.
- `length`: Maximum length of the string to copy.

## See Also

### Creating a String
- [withString](./withstring.md)
  Allocates an OSString object with a copy of an OString object.
- [withCString](./withcstring-4wsql.md)
  Allocates an OSString object with a copy of a c-string.
- [withCStringNoCopy](./withcstringnocopy.md)
  Allocates an OSString object with a copy of a c-string.
- [OSStringCreate](../osstringcreate.md)
- [free](./free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring/withcstring-721oh)*