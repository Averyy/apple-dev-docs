# location

**Framework**: Foundation  
**Kind**: property

The index of the first member of the range.

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
var location: Int
```

#### Discussion

The minimum first index is `0`, as in C arrays. For type compatibility with the rest of the system, the maximum value you should use for the location is `LONG_MAX`.

## See Also

- [var length: Int](nsrange-swift.typealias/length.md)
  The number of items in the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrange-swift.typealias/location)*