# AsyncThrowingFlatMapSequence.Failure

**Framework**: Swift  
**Kind**: typealias

The type of error produced by this asynchronous sequence.

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
typealias Failure = any Error
```

#### Discussion

The flat map sequence produces errors from either the base sequence or the `transform` closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingflatmapsequence/failure)*