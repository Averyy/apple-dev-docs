# endIndex

**Framework**: Foundation  
**Kind**: property

The end index into the data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var endIndex: Data.Index { get }
```

#### Discussion

This is the “one-past-the-end” position, and will always be equal to the `count`.

## See Also

- [typealias Index](data/index.md)
  A type used to indicate a position in a data’s buffer.
- [var startIndex: Data.Index](data/startindex.md)
  The beginning index into the data.
- [func index(after: Data.Index) -> Data.Index](data/index(after:).md)
  Returns the index that immediately follows the specified index.
- [func index(before: Data.Index) -> Data.Index](data/index(before:).md)
  Returns the index that immediately precedes the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/endindex)*