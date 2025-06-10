# map(_:)

**Framework**: Swift  
**Kind**: method

Returns a `LazyMapSequence` over this `Sequence`.  The elements of the result are computed lazily, each time they are read, by calling `transform` function on a base element.

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
func map<U>(_ transform: @escaping (Self.Element) -> U) -> LazyMapSequence<Self.Elements, U>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/reversedcollection/map(_:)-88nu3)*