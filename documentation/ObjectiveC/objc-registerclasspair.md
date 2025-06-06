# objc_registerClassPair(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Registers a class that was allocated using [`objc_allocateClassPair(_:_:_:)`](objc_allocateclasspair(_:_:_:).md).

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
func objc_registerClassPair(_ cls: AnyClass)
```

## Parameters

- `cls`: The class you want to register.

## See Also

- [func objc_allocateClassPair(AnyClass?, UnsafePointer<CChar>, Int) -> AnyClass?](objc_allocateclasspair(_:_:_:).md)
  Creates a new class and metaclass.
- [func objc_disposeClassPair(AnyClass)](objc_disposeclasspair(_:).md)
  Destroys a class and its associated metaclass.
- [func objc_duplicateClass(AnyClass, UnsafePointer<CChar>, Int) -> AnyClass](objc_duplicateclass(_:_:_:).md)
  Used by Foundation’s Key-Value Observing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_registerclasspair(_:))*