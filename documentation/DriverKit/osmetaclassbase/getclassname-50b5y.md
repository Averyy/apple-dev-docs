# GetClassName

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the name of the class given an OSObject pointer.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
const char * GetClassName();
```

## Return Value

C-string class name, valid while the object is retained.

## See Also

### Getting Meta Information
- [IsRemote](./isremote.md)
- [GetClass](./getclass.md)
  Internal helper for GetClassName. Not to be called directly.
- [getMetaClass](./getmetaclass.md)
  Internal helper for GetClassName. Not to be called directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osmetaclassbase/getclassname-50b5y)*