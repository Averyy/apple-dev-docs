# init(from:)

**Framework**: RealityKit  
**Kind**: init

Loads a configuration catalog from a USD or reality file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(from url: URL) async throws
```

#### Discussion

This method parses a USD or `.reality` file, and provides a collection of available configurations based on USD variant sets or `.reality` file configurations. It doesn’t load large asset files, such as textures and meshes.

You can load an entity, and its assets, with configuration choices by calling [`init(from:configurations:)`](entity/init(from:configurations:).md).

## Parameters

- `url`: A URL of a USD or   file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog-2tett/init(from:))*