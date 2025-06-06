# init(named:from:)

**Framework**: RealityKit  
**Kind**: init

Loads a ShaderGraphMaterial from a url.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(named name: String, from url: URL) async throws
```

#### Return Value

A ShaderGraphMaterial object from the file with the name specified.

#### Discussion

Supported file formats are USD (.usd, .usda, .usdc, .usdz) and Reality File (.reality).

## Parameters

- `name`: The name of the ShaderGraphMaterial within the file.   For USD files, this is the full path of the material prim (such as “/Root/MyMaterial”).
- `url`: The path or address of the file containing the ShaderGraphMaterial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraphmaterial/init(named:from:)-52t12)*