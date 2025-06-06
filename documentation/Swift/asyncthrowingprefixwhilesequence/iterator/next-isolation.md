# next(isolation:)

**Framework**: Swift  
**Kind**: method

Produces the next element in the prefix-while sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws -> Base.Element?
```

#### Discussion

If the predicate hasn’t failed yet, this method gets the next element from the base sequence and calls the predicate with it. If this call succeeds, this method passes along the element. Otherwise, it returns `nil`, ending the sequence. If calling the predicate closure throws an error, the sequence ends and `next(isolation:)` rethrows the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingprefixwhilesequence/iterator/next(isolation:))*