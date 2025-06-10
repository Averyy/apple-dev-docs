# init(from:configurations:)

**Framework**: RealityKit  
**Kind**: init

Loads an entity from a configuration catalog and a dictionary of configuration choices.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(from catalog: Entity.ConfigurationCatalog, configurations: [String : String]? = nil) async throws
```

## Parameters

- `catalog`: A collection of alternative representations for an entity.
- `configurations`: A dictionary of configuration choices the initializer applies as it loads the entity,   mapping the ID of a configuration set to the ID of a configuration within that set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/init(from:configurations:))*