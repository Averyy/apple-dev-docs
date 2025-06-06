# applying(_:)

**Framework**: Swift  
**Kind**: method

Applies the given difference to this collection.

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
func applying(_ difference: CollectionDifference<Self.Element>) -> Self?
```

#### Return Value

An instance representing the state of the receiver with the difference applied, or `nil` if the difference is incompatible with the receiver’s state.

#### Discussion

> **Note**: O( + ), where  is `self.count` and  is the number of changes contained by the parameter.

## Parameters

- `difference`: The difference to be applied.

## See Also

- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](string/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](string/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/applying(_:))*