# isContiguousUTF8

**Framework**: Swift  
**Kind**: property

Returns whether this string’s storage contains validly-encoded UTF-8 contents in contiguous memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isContiguousUTF8: Bool { get }
```

#### Discussion

Contiguous strings always operate in O(1) time for withUTF8, always give a result for Substring.UTF8View.withContiguousStorageIfAvailable, and always return a non-nil value from `Substring._utf8Span` and `Substring.UTF8View._span`. Contiguous strings also benefit from fast-paths and better optimizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/iscontiguousutf8)*