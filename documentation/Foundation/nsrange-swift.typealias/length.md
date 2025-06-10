# length

**Framework**: Foundation  
**Kind**: property

The number of items in the range.

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
var length: Int
```

#### Discussion

This value can be `0` to represent an empty range. For type compatibility with the rest of the system, the maximum value you should use for length is `LONG_MAX`.

## See Also

- [var location: Int](nsrange-swift.typealias/location.md)
  The index of the first member of the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsrange-swift.typealias/length)*