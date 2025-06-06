# pointer(at:)

**Framework**: Foundation  
**Kind**: method

Returns the pointer at a given index.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func pointer(at index: Int) -> UnsafeMutableRawPointer?
```

#### Return Value

The pointer at `index`.

#### Discussion

The returned value may be `NULL`.

## Parameters

- `index`: The index of an element in the receiver. This value must be less than the   of the receiver.

## See Also

- [var count: Int](nspointerarray/count.md)
  The number of elements in the receiver.
- [var allObjects: [Any]](nspointerarray/allobjects.md)
  All the objects in the receiver.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray/pointer(at:))*