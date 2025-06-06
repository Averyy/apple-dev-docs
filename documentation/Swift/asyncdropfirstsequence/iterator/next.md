# next()

**Framework**: Swift  
**Kind**: method

Produces the next element in the drop-first sequence.

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

Until reaching the number of elements to drop, this iterator calls `next()` on its base iterator and discards the result. If the base iterator returns `nil`, indicating the end of the sequence, this iterator returns `nil`. After reaching the number of elements to drop, this iterator passes along the result of calling `next()` on the base iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncdropfirstsequence/iterator/next())*