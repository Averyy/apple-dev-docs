# ivar_getOffset(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the offset of an instance variable.

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
func ivar_getOffset(_ v: Ivar) -> Int
```

#### Discussion

For instance variables of type `id` or other object types, call [`object_getIvar(_:_:)`](object_getivar(_:_:).md) and [`object_setIvar(_:_:_:)`](object_setivar(_:_:_:).md) instead of using this offset to access the instance variable data directly.

## See Also

- [func ivar_getName(Ivar) -> UnsafePointer<CChar>?](ivar_getname(_:).md)
  Returns the name of an instance variable.
- [func ivar_getTypeEncoding(Ivar) -> UnsafePointer<CChar>?](ivar_gettypeencoding(_:).md)
  Returns the type string of an instance variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/ivar_getoffset(_:))*