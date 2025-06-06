# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new collection difference from a collection of changes.

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
init?<Changes>(_ changes: Changes) where Changes : Collection, Changes.Element == CollectionDifference<ChangeElement>.Change
```

#### Discussion

To find the difference between two collections, use the `difference(from:)` method declared on the `BidirectionalCollection` protocol.

The collection of changes passed as `changes` must meet these requirements:

- All insertion offsets are unique
- All removal offsets are unique
- All associations between insertions and removals are symmetric

> **Note**: O( * log()), where  is the length of the parameter.

## Parameters

- `changes`: A collection of changes that represent a transition   between two states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collectiondifference/init(_:))*