# write(to:options:)

**Framework**: RealityKit  
**Kind**: method

Writes the configurations of the configuration catalog to a reality file.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
(nonsending) func write(to url: URL, options: Entity.WriteOptions) async throws
```

#### Discussion

Another configuration catalog instance can open the `.reality` file for reading.

## Parameters

- `url`: The destination where the configuration catalog writes the `.reality` file.
- `options`: Options for writing the `.reality` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/configurationcatalog/write(to:options:))*