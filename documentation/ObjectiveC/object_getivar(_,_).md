# object_getIvar(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Reads the value of an instance variable in an object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func object_getIvar(_ obj: Any?, _ ivar: Ivar) -> Any?
```

```c
extern idobject_getIvar(id obj, Ivar ivar);
```

## Return Value

The value of the instance variable specified by `ivar`, or `nil` if `object` is `nil`.

## Discussion

[`object_getIvar(_:_:)`](./object_getivar%28_,_%29.md) is faster than [`object_getInstanceVariable`](./object_getinstancevariable.md) if the Ivar for the instance variable is already known.

## Parameters

- `obj`: The object containing the instance variable whose value you want to read.
- `ivar`: The Ivar describing the instance variable whose value you want to read.

## See Also

### Working with Instances
- [func object_getIndexedIvars(Any?) -> UnsafeMutableRawPointer?](./object_getindexedivars%28_%29.md)
  Returns a pointer to any extra bytes allocated with a instance given object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/object_getivar(_:_:))*