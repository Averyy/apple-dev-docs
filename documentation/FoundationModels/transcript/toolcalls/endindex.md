# endIndex

**Framework**: Foundation Models  
**Kind**: property

The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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

- [var id: String](transcript/toolcalls/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [Transcript.ToolCalls.ID](transcript/toolcalls/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
- [var startIndex: Int](transcript/toolcalls/startindex.md)
  The position of the first element in a nonempty collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcript/toolcalls/endindex)*