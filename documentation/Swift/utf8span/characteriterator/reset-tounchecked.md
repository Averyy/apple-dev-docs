# reset(toUnchecked:)

**Framework**: Swift  
**Kind**: method

Reset this iterator to `codeUnitOffset`, skipping  safety checks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
mutating func reset(toUnchecked codeUnitOffset: Int)
```

#### Discussion

Note: This is only for very specific, low-level use cases. If `codeUnitOffset` is not properly scalar-aligned, this function can result in undefined behavior when, e.g., `next()` is called.

If `i` is scalar-aligned, but not `Character`-aligned, you may get different results from running `Character` iteration.

For example, this could be used by a regex engine to backtrack to a known-valid previous position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/characteriterator/reset(tounchecked:))*