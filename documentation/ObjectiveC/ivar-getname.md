# ivar_getName(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the name of an instance variable.

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
func ivar_getName(_ v: Ivar) -> UnsafePointer<CChar>?
```

#### Return Value

A C string containing the instance variable’s name.

## See Also

- [func ivar_getTypeEncoding(Ivar) -> UnsafePointer<CChar>?](ivar_gettypeencoding(_:).md)
  Returns the type string of an instance variable.
- [func ivar_getOffset(Ivar) -> Int](ivar_getoffset(_:).md)
  Returns the offset of an instance variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/ivar_getname(_:))*