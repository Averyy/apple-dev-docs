# object_getClassName(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the class name of a given object.

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
func object_getClassName(_ obj: Any?) -> UnsafePointer<CChar>
```

#### Return Value

The name of the class of which `obj` is an instance.

## Parameters

- `obj`: An Objective-C object.

## See Also

- [func object_getIndexedIvars(Any?) -> UnsafeMutableRawPointer?](object_getindexedivars(_:).md)
  Returns a pointer to any extra bytes allocated with a instance given object.
- [func object_getIvar(Any?, Ivar) -> Any?](object_getivar(_:_:).md)
  Reads the value of an instance variable in an object.
- [func object_setIvar(Any?, Ivar, Any?)](object_setivar(_:_:_:).md)
  Sets the value of an instance variable in an object.
- [func object_getClass(Any?) -> AnyClass?](object_getclass(_:).md)
  Returns the class of an object.
- [func object_setClass(Any?, AnyClass) -> AnyClass?](object_setclass(_:_:).md)
  Sets the class of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/object_getclassname(_:))*