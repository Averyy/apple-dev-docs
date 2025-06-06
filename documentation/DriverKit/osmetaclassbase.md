# OSMetaClassBase

**Framework**: DriverKit  
**Kind**: class

Base class for DriverKit objects.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class OSMetaClassBase;
```

## Topics

### Managing the Object Lifecycle
- [retain](osmetaclassbase/retain.md)
  Retains the OSObject instance
- [release](osmetaclassbase/release.md)
  Releases the OSObject instance
### Casting to Different Types
- [requiredMetaCast](osmetaclassbase/requiredmetacast.md)
  Internal helper for OSRequiredCast. Not to be called directly.
- [safeMetaCast](osmetaclassbase/safemetacast.md)
  Internal helper for OSDynamicCast. Not to be called directly.
### Getting Meta Information
- [IsRemote](osmetaclassbase/isremote.md)
- [GetClass](osmetaclassbase/getclass.md)
  Internal helper for GetClassName. Not to be called directly.
- [GetClassName](osmetaclassbase/getclassname-50b5y.md)
  Returns the name of the class given an OSObject pointer.
- [getMetaClass](osmetaclassbase/getmetaclass.md)
  Internal helper for GetClassName. Not to be called directly.
### Comparing Objects
- [isEqualTo](osmetaclassbase/isequalto.md)
  Compares two objects
### Managing Runtime Internals
- [Invoke](osmetaclassbase/invoke.md)
  Runtime internals
- [Dispatch](osmetaclassbase/dispatch.md)
  Runtime internals
### Instance Methods
- [GetClassName](osmetaclassbase/getclassname-r83c.md)
- [getRetainCount](osmetaclassbase/getretaincount.md)
- [operator new](osmetaclassbase/operator_new.md)
### Instance Properties
- [meta](osmetaclassbase/meta.md)
- [refcount](osmetaclassbase/refcount.md)
- [reserved](osmetaclassbase/reserved.md)

## Relationships

### Inherited By
- [OSMetaClass](osmetaclass.md)
- [OSObject](osobject.md)

## See Also

- [OSMetaClass](osmetaclass.md)
  Base class for DriverKit runtime class system. Not called directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osmetaclassbase)*