# removePointer(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the pointer at a given index.

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
func removePointer(at index: Int)
```

```objc
- (void) removePointerAtIndex:(NSUInteger) index;
```

## Discussion

Elements above `index`, including `NULL` values, slide lower.

## Parameters

- `index`: The index of an element in the receiver. This value must be less than the [`count`](./count.md) of the receiver.

## See Also

### Managing the Collection
- [var count: Int](./count.md)
  The number of elements in the receiver.
- [var allObjects: [Any]](./allobjects.md)
  All the objects in the receiver.
- [func pointer(at: Int) -> UnsafeMutableRawPointer?](./pointer%28at%29.md)
  Returns the pointer at a given index.
- [func addPointer(UnsafeMutableRawPointer?)](./addpointer%28_%29.md)
  Adds a given pointer to the receiver.
- [func insertPointer(UnsafeMutableRawPointer?, at: Int)](./insertpointer%28_,at%29.md)
  Inserts a pointer at a given index.
- [func replacePointer(at: Int, withPointer: UnsafeMutableRawPointer?)](./replacepointer%28at,withpointer%29.md)
  Replaces the pointer at a given index.
- [func compact()](./compact%28%29.md)
  Removes `NULL` values from the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nspointerarray/removepointer(at:))*