# trimPrefix(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Removes `prefix` from the start of the collection.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
mutating func trimPrefix<Prefix>(_ prefix: Prefix) where Prefix : Sequence, Self.Element == Prefix.Element
```

Available when `Self` is `Self.SubSequence` and `Element` conforms to `Equatable`.

## Parameters

- `prefix`: The collection to remove from this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/trimprefix(_:))*