# append(contentsOf:)

**Framework**: App Intents  
**Kind**: method

Adds the identifiers for multiple entities to the collection.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
mutating func append(contentsOf entities: [Entity])
```

#### Discussion

- Parameter: - entities: An array of entities. This method adds the identifier for each entity to the collection.

This method adds the identifier for each entity to the collection, but doesn’t keep a reference to the actual entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitycollection/append(contentsof:)-7zah3)*