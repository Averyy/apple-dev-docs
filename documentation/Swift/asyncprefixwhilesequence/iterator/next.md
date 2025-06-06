# next()

**Framework**: Swift  
**Kind**: method

Produces the next element in the prefix-while sequence.

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

If the predicate hasn’t yet failed, this method gets the next element from the base sequence and calls the predicate with it. If this call succeeds, this method passes along the element. Otherwise, it returns `nil`, ending the sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncprefixwhilesequence/iterator/next())*