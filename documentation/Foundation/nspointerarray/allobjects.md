# allObjects

**Framework**: Foundation  
**Kind**: property

All the objects in the receiver.

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

## See Also

- [var count: Int](nspointerarray/count.md)
  The number of elements in the receiver.
- [func pointer(at: Int) -> UnsafeMutableRawPointer?](nspointerarray/pointer(at:).md)
  Returns the pointer at a given index.
- [func addPointer(UnsafeMutableRawPointer?)](nspointerarray/addpointer(_:).md)
  Adds a given pointer to the receiver.
- [func removePointer(at: Int)](nspointerarray/removepointer(at:).md)
  Removes the pointer at a given index.
- [func insertPointer(UnsafeMutableRawPointer?, at: Int)](nspointerarray/insertpointer(_:at:).md)
  Inserts a pointer at a given index.
- [func replacePointer(at: Int, withPointer: UnsafeMutableRawPointer?)](nspointerarray/replacepointer(at:withpointer:).md)
  Replaces the pointer at a given index.
- [func compact()](nspointerarray/compact.md)
  Removes `NULL` values from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray/allobjects)*