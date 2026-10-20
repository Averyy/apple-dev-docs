# next()

**Framework**: Swift  
**Kind**: method

Produces the next element in the flat map sequence.

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
mutating func next() async throws -> SegmentOfResult.Element?
```

#### Discussion

This iterator calls `next()` on its base iterator; if this call returns `nil`, `next()` returns `nil`. Otherwise, `next()` calls the transforming closure on the received element, takes the resulting asynchronous sequence, and creates an asynchronous iterator from it. `next()` then consumes values from this iterator until it terminates. At this point, `next()` is ready to receive the next value from the base sequence. If `transform` throws an error, the sequence terminates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingflatmapsequence/iterator/next())*