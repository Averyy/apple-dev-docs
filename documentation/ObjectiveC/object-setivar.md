# object_setIvar(_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Sets the value of an instance variable in an object.

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
func object_setIvar(_ obj: Any?, _ ivar: Ivar, _ value: Any?)
```

#### Discussion

[`object_setIvar(_:_:_:)`](object_setivar(_:_:_:).md) is faster than [`object_setInstanceVariable`](object_setinstancevariable.md) if the Ivar for the instance variable is already known.

## Parameters

- `obj`: The object containing the instance variable whose value you want to set.
- `ivar`: The Ivar describing the instance variable whose value you want to set.
- `value`: The new value for the instance variable.

## See Also

- [func object_getIndexedIvars(Any?) -> UnsafeMutableRawPointer?](object_getindexedivars(_:).md)
  Returns a pointer to any extra bytes allocated with a instance given object.
- [func object_getIvar(Any?, Ivar) -> Any?](object_getivar(_:_:).md)
  Reads the value of an instance variable in an object.
- [func object_getClassName(Any?) -> UnsafePointer<CChar>](object_getclassname(_:).md)
  Returns the class name of a given object.
- [func object_getClass(Any?) -> AnyClass?](object_getclass(_:).md)
  Returns the class of an object.
- [func object_setClass(Any?, AnyClass) -> AnyClass?](object_setclass(_:_:).md)
  Sets the class of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/object_setivar(_:_:_:))*