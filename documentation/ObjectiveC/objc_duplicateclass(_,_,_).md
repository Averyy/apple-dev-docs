# objc_duplicateClass(_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Used by Foundation’s Key-Value Observing.

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
func objc_duplicateClass(_ original: AnyClass, _ name: UnsafePointer<CChar>, _ extraBytes: Int) -> AnyClass
```

#### Discussion

Do not call this function yourself.

## See Also

- [func objc_allocateClassPair(AnyClass?, UnsafePointer<CChar>, Int) -> AnyClass?](objc_allocateclasspair(_:_:_:).md)
  Creates a new class and metaclass.
- [func objc_disposeClassPair(AnyClass)](objc_disposeclasspair(_:).md)
  Destroys a class and its associated metaclass.
- [func objc_registerClassPair(AnyClass)](objc_registerclasspair(_:).md)
  Registers a class that was allocated using [`objc_allocateClassPair(_:_:_:)`](objc_allocateclasspair(_:_:_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_duplicateclass(_:_:_:))*