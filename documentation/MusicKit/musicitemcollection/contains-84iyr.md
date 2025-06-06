# contains(_:)

**Framework**: MusicKit  
**Kind**: method

Returns a Boolean value indicating whether the collection contains the given sequence.

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
func contains<C>(_ other: C) -> Bool where C : Collection, Self.Element == C.Element
```

#### Return Value

`true` if the collection contains the specified sequence, otherwise `false`.

## Parameters

- `other`: A sequence to search for within this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicitemcollection/contains(_:)-84iyr)*