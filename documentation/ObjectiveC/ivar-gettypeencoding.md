# ivar_getTypeEncoding(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the type string of an instance variable.

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
func ivar_getTypeEncoding(_ v: Ivar) -> UnsafePointer<CChar>?
```

#### Return Value

A C string containing the instance variable’s type encoding.

#### Discussion

For possible values, see [`Objective-C Runtime Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048) > [`Type Encodings`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html#//apple_ref/doc/uid/TP40008048-CH100).

## See Also

- [func ivar_getName(Ivar) -> UnsafePointer<CChar>?](ivar_getname(_:).md)
  Returns the name of an instance variable.
- [func ivar_getOffset(Ivar) -> Int](ivar_getoffset(_:).md)
  Returns the offset of an instance variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/ivar_gettypeencoding(_:))*