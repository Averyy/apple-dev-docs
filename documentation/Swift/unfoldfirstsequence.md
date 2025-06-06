# UnfoldFirstSequence

**Framework**: Swift  
**Kind**: typealias

The return type of `sequence(first:next:)`.

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
typealias UnfoldFirstSequence<T> = UnfoldSequence<T, (T?, Bool)>
```

## See Also

- [UnfoldSequence.Iterator](unfoldsequence/iterator.md)
  A type that provides the sequence’s iteration interface and encapsulates its iteration state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unfoldfirstsequence)*