# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance of a collection containing the elements of a sequence.

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
init<S>(_ elements: S) where S : Sequence, S.Element == Character
```

## Parameters

- `elements`: The sequence of elements for the new collection.    must be finite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/init(_:)-6lxbv)*