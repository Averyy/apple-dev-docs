# init(named:from:)

**Framework**: RealityKit  
**Kind**: init

Loads a ShaderGraphMaterial from a named material within a USD file.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(named name: String, from data: Data) async throws
```

#### Return Value

A ShaderGraphMaterial object from the file with the name specified.

#### Discussion

Supported file formats are USD (.usd, .usda, .usdc, .usdz)

## Parameters

- `name`: The name of the ShaderGraphMaterial within the USD file.
- `data`: A data object containing USD file data


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/init(named:from:)-9qt59)*