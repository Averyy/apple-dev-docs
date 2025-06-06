# endIndex

**Framework**: Create ML  
**Kind**: property

The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var endIndex: Int { get }
```

#### Discussion

When you need a range that includes the last element of a collection, use the half-open range operator (`..<`) with `endIndex`. The `..<` operator creates a range that doesn’t include the upper bound, so it’s always safe to use with `endIndex`. For example:

```None
let numbers = [10, 20, 30, 40, 50]
if let index = numbers.firstIndex(of: 30) {
    print(numbers[index ..< numbers.endIndex])
}
// Prints "[30, 40, 50]"
```

If the collection is empty, `endIndex` is equal to `startIndex`.

## See Also

- [var startIndex: Int](mldatatable/row/values-swift.struct/startindex.md)
  The position of the first element in a nonempty collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/values-swift.struct/endindex)*