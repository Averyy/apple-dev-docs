# append(contentsOf:)

**Framework**: App Intents  
**Kind**: method

Adds the identifiers for multiple entities to the collection.

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
mutating func append(contentsOf entities: [Entity])
```

#### Discussion

- Parameter: - entities: An array of entities. This method adds the identifier for each entity to the collection.

This method adds the identifier for each entity to the collection, but doesn’t keep a reference to the actual entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitycollection/append(contentsof:)-7zah3)*