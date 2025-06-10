# init(materialXLabel:data:)

**Framework**: RealityKit  
**Kind**: init

Loads a ShaderGraphMaterial from MaterialX data.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
init(materialXLabel: String, data: Data) async throws
```

#### Return Value

A ShaderGraphMaterial object from the data with the label specified.

## Parameters

- `materialXLabel`: The name of the ShaderGraphMaterial in the MaterialX data.
- `data`: The data containing the MaterialX file contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/init(materialxlabel:data:))*