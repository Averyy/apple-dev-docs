# AsyncPrefixWhileSequence.Failure

**Framework**: Swift  
**Kind**: typealias  
**Role**: Type Alias

The type of the error that can be produced by the sequence.

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
typealias Failure = Base.Failure
```

Available when `Base` conforms to `AsyncSequence`.

## Discussion

The prefix-while sequence produces whatever type of error its base sequence does.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncprefixwhilesequence/failure)*