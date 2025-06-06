# GetClassName

**Framework**: DriverKit  
**Kind**: method

Returns the name of the class given an OSObject pointer.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
const char * GetClassName();
```

#### Return Value

C-string class name, valid while the object is retained.

## See Also

- [IsRemote](osmetaclassbase/isremote.md)
- [GetClass](osmetaclassbase/getclass.md)
  Internal helper for GetClassName. Not to be called directly.
- [getMetaClass](osmetaclassbase/getmetaclass.md)
  Internal helper for GetClassName. Not to be called directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osmetaclassbase/getclassname-50b5y)*