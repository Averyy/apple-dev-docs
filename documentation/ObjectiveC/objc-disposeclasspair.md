# objc_disposeClassPair(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Destroys a class and its associated metaclass.

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
func objc_disposeClassPair(_ cls: AnyClass)
```

#### Discussion

Do not call this function if instances of the `cls` class or any subclass exist.

## Parameters

- `cls`: The class to be destroyed. This class must have been allocated using  .

## See Also

- [func objc_allocateClassPair(AnyClass?, UnsafePointer<CChar>, Int) -> AnyClass?](objc_allocateclasspair(_:_:_:).md)
  Creates a new class and metaclass.
- [func objc_registerClassPair(AnyClass)](objc_registerclasspair(_:).md)
  Registers a class that was allocated using [`objc_allocateClassPair(_:_:_:)`](objc_allocateclasspair(_:_:_:).md).
- [func objc_duplicateClass(AnyClass, UnsafePointer<CChar>, Int) -> AnyClass](objc_duplicateclass(_:_:_:).md)
  Used by Foundation’s Key-Value Observing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_disposeclasspair(_:))*