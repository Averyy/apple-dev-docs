# replaceSubrange(_:addingCount:initializingWith:)

**Framework**: Swift  
**Kind**: method

Replaces the specified range of elements by a given count of new items, using a callback to directly initialize array storage by populating an output span.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
mutating func replaceSubrange<E>(_ subrange: Range<Int>, addingCount newItemCount: Int, initializingWith initializer: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

The number of new items need not match the number of elements being removed.

This method has the same overall effect as calling

```swift
try array.removeSubrange(subrange)
try array.insert(
  addingCount: newItemCount,
  at: subrange.lowerBound,
  initializingWith: initializer)
```

Except it performs faster (by a constant factor), by avoiding moving some items in the array twice.

If the array does not have sufficient capacity to perform the replacement, then this reallocates storage to extend its capacity, using a geometric growth rate.

If the callback fails to fully populate its output span or if it throws an error, then the array keeps all items that were successfully initialized before the callback terminated the prepend.

Partial insertions create a gap in array storage that needs to be closed by moving newly inserted items to their correct positions given the adjusted count. This adds some overhead compared to adding exactly as many items as promised.

> **Note**: O(`self.count` + `newItemCount`) in addition to the complexity of the callback invocations.

## Parameters

- `subrange`: The subrange of the array to replace. The bounds of the range must be valid indices in the array.
- `newItemCount`: The maximum number of items to replace the old subrange.
- `initializer`: A callback that gets called at most once to directly populate newly reserved storage within the array. The function is always called with an empty output span.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/replacesubrange(_:addingcount:initializingwith:))*