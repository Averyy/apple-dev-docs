# objc_duplicateClass(_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

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

```c
extern Classobjc_duplicateClass(Class original, const char *name, size_t extraBytes);
```

## Discussion

Do not call this function yourself.

## See Also

### Adding Classes
- [func objc_allocateClassPair(AnyClass?, UnsafePointer<CChar>, Int) -> AnyClass?](./objc_allocateclasspair%28_,_,_%29.md)
  Creates a new class and metaclass.
- [func objc_disposeClassPair(AnyClass)](./objc_disposeclasspair%28_%29.md)
  Destroys a class and its associated metaclass.
- [func objc_registerClassPair(AnyClass)](./objc_registerclasspair%28_%29.md)
  Registers a class that was allocated using [`objc_allocateClassPair(_:_:_:)`](./objc_allocateclasspair%28_,_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_duplicateclass(_:_:_:))*