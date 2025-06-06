# objc_allocateClassPair(_:_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Creates a new class and metaclass.

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
func objc_allocateClassPair(_ superclass: AnyClass?, _ name: UnsafePointer<CChar>, _ extraBytes: Int) -> AnyClass?
```

#### Return Value

The new class, or `Nil` if the class could not be created (for example, the desired name is already in use).

#### Discussion

You can get a pointer to the new metaclass by calling `object_getClass(newClass)`.

To create a new class, start by calling [`objc_allocateClassPair(_:_:_:)`](objc_allocateclasspair(_:_:_:).md). Then set the class’s attributes with functions like [`class_addMethod(_:_:_:_:)`](class_addmethod(_:_:_:_:).md) and [`class_addIvar(_:_:_:_:_:)`](class_addivar(_:_:_:_:_:).md). When you are done building the class, call [`objc_registerClassPair(_:)`](objc_registerclasspair(_:).md). The new class is now ready for use.

Instance methods and instance variables should be added to the class itself. Class methods should be added to the metaclass.

## Parameters

- `superclass`: The class to use as the new class’s superclass, or   to create a new root class.
- `name`: The string to use as the new class’s name. The string will be copied.
- `extraBytes`: The number of bytes to allocate for indexed ivars at the end of the class and metaclass objects. This should usually be  .

## See Also

- [func objc_disposeClassPair(AnyClass)](objc_disposeclasspair(_:).md)
  Destroys a class and its associated metaclass.
- [func objc_registerClassPair(AnyClass)](objc_registerclasspair(_:).md)
  Registers a class that was allocated using [`objc_allocateClassPair(_:_:_:)`](objc_allocateclasspair(_:_:_:).md).
- [func objc_duplicateClass(AnyClass, UnsafePointer<CChar>, Int) -> AnyClass](objc_duplicateclass(_:_:_:).md)
  Used by Foundation’s Key-Value Observing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_allocateclasspair(_:_:_:))*