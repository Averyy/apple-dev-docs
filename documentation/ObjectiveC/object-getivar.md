# object_getIvar(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

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

#### Return Value

The value of the instance variable specified by `ivar`, or `nil` if `object` is `nil`.

#### Discussion

[`object_getIvar(_:_:)`](object_getivar(_:_:).md) is faster than [`object_getInstanceVariable`](object_getinstancevariable.md) if the Ivar for the instance variable is already known.

## Parameters

- `obj`: The object containing the instance variable whose value you want to read.
- `ivar`: The Ivar describing the instance variable whose value you want to read.

## See Also

- [func object_getIndexedIvars(Any?) -> UnsafeMutableRawPointer?](object_getindexedivars(_:).md)
  Returns a pointer to any extra bytes allocated with a instance given object.
- [func object_setIvar(Any?, Ivar, Any?)](object_setivar(_:_:_:).md)
  Sets the value of an instance variable in an object.
- [func object_getClassName(Any?) -> UnsafePointer<CChar>](object_getclassname(_:).md)
  Returns the class name of a given object.
- [func object_getClass(Any?) -> AnyClass?](object_getclass(_:).md)
  Returns the class of an object.
- [func object_setClass(Any?, AnyClass) -> AnyClass?](object_setclass(_:_:).md)
  Sets the class of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/object_getivar(_:_:))*