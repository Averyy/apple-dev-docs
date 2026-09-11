# init(position:)

**Framework**: SwiftUI  
**Kind**: init

Initializes the destination value with the provided position and an instance of `ReorderableSingleCollectionIdentifier`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(position: ReorderDifference<ItemID, CollectionID>.Destination.Position) where CollectionID == ReorderableSingleCollectionIdentifier
```

#### Discussion

- position: The position within the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/reorderdifference/destination-swift.struct/init(position:))*