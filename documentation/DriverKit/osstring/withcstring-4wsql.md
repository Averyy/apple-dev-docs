# withCString

**Framework**: DriverKit  
**Kind**: method

Allocates an OSString object with a copy of a c-string.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
static OSStringPtr withCString(const char * cString);
```

#### Return Value

NULL on failure, otherwise the allocated OSString with reference count 1 to be released by the caller.

## Parameters

- `cString`: Pointer to null terminated c-string. The string will be copied at the time of the call.

## See Also

- [withString](osstring/withstring.md)
  Allocates an OSString object with a copy of an OString object.
- [withCString](osstring/withcstring-721oh.md)
  Allocates an OSString object with a copy of a c-string, up to a given length.
- [withCStringNoCopy](osstring/withcstringnocopy.md)
  Allocates an OSString object with a copy of a c-string.
- [OSStringCreate](osstringcreate.md)
- [free](osstring/free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osstring/withcstring-4wsql)*