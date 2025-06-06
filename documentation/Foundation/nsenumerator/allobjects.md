# allObjects

**Framework**: Foundation  
**Kind**: property

The array of unenumerated objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var allObjects: [Any] { get }
```

#### Discussion

This array contains all the remaining objects of the enumerator in enumerated order. It does not contain objects that have already been enumerated with previous [`nextObject()`](nsenumerator/nextobject().md) messages.

Accessing this property exhausts the enumerator’s collection so that subsequent invocations of [`nextObject()`](nsenumerator/nextobject().md) return `nil`.

## See Also

- [Collections Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [func nextObject() -> Any?](nsenumerator/nextobject.md)
  Returns the next object from the collection being enumerated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsenumerator/allobjects)*