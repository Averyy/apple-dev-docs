# next()

**Framework**: Swift  
**Kind**: method

Produces the next element in the prefix sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
mutating func next() async rethrows -> Base.Element?
```

#### Discussion

Until reaching the number of elements to include, this iterator calls `next()` on its base iterator and passes through the result. After reaching the maximum number of elements, subsequent calls to `next()` return `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncprefixsequence/iterator/next())*