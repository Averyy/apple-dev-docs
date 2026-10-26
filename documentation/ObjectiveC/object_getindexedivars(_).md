# object_getIndexedIvars(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns a pointer to any extra bytes allocated with a instance given object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func object_getIndexedIvars(_ obj: Any?) -> UnsafeMutableRawPointer?
```

```c
extern void *object_getIndexedIvars(id obj);
```

#### Return Value

A pointer to any extra bytes allocated with `obj`. If `obj` was not allocated with any extra bytes, then dereferencing the returned pointer is undefined.

#### Discussion

This function returns a pointer to any extra bytes allocated with the instance (as specified by [`class_createInstance(_:_:)`](./class_createinstance%28_,_%29.md) with extraBytes>0). This memory follows the object’s ordinary ivars, but may not be adjacent to the last ivar.

The returned pointer is guaranteed to be pointer-size aligned, even if the area following the object’s last ivar is less aligned than that. Alignment greater than pointer-size is never guaranteed, even if the area following the object’s last ivar is more aligned than that.

In a garbage-collected environment, the memory is scanned conservatively.

## Parameters

- `obj`: An Objective-C object.

## See Also

### Working with Instances
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
- [object_copy](./object_copy.md)
  Returns a copy of a given object.
- [object_dispose](./object_dispose.md)
  Frees the memory occupied by a given object.
- [object_setInstanceVariable](./object_setinstancevariable.md)
  Changes the value of an instance variable of a class instance.
- [object_getInstanceVariable](./object_getinstancevariable.md)
  Obtains the value of an instance variable of a class instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/object_getindexedivars(_:))*