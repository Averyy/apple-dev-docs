# makeIterator()

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns an iterator for this sequence.

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
func makeIterator() -> PartialRangeFrom<Bound>.Iterator
```

Available when `Bound` conforms to `Strideable` and `Bound.Stride` conforms to `SignedInteger`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/partialrangefrom/makeiterator())*