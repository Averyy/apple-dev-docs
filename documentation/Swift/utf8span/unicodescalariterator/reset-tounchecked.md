# reset(toUnchecked:)

**Framework**: Swift  
**Kind**: method

Reset this iterator to `codeUnitOffset`, skipping  safety checks (including bounds checks).

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func reset(toUnchecked codeUnitOffset: Int)
```

#### Discussion

Note: This is only for very specific, low-level use cases. If `codeUnitOffset` is not properly scalar-aligned, this function can result in undefined behavior when, e.g., `next()` is called.

TODO: verify that we’re not UB, just garabage-data or guaranteed trap!

For example, this could be used by a regex engine to backtrack to a known-valid previous position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/utf8span/unicodescalariterator/reset(tounchecked:))*