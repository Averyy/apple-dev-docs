# object_dispose

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Frees the memory occupied by a given object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```c
extern idobject_dispose(id obj);
```

## Return Value

`nil`.

## Parameters

- `obj`: An Objective-C object.

## See Also

### Working with Instances
- [object_copy](./object_copy.md)
  Returns a copy of a given object.
- [object_setInstanceVariable](./object_setinstancevariable.md)
  Changes the value of an instance variable of a class instance.
- [object_getInstanceVariable](./object_getinstancevariable.md)
  Obtains the value of an instance variable of a class instance.
- [func object_getIndexedIvars(Any?) -> UnsafeMutableRawPointer?](./object_getindexedivars%28_%29.md)
  Returns a pointer to any extra bytes allocated with a instance given object.
- [func object_getIvar(Any?, Ivar) -> Any?](./object_getivar%28_,_%29.md)
  Reads the value of an instance variable in an object.
- [func object_setIvar(Any?, Ivar, Any?)](./object_setivar%28_,_,_%29.md)
  Sets the value of an instance variable in an object.
- [func object_getClassName(Any?) -> UnsafePointer<CChar>](./object_getclassname%28_%29.md)
  Returns the class name of a given object.
- [func object_getClass(Any?) -> AnyClass?](./object_getclass%28_%29.md)
  Returns the class of an object.
- [func object_setClass(Any?, AnyClass) -> AnyClass?](./object_setclass%28_,_%29.md)
  Sets the class of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/object_dispose)*