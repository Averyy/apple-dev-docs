---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/image"
framework: "mlx-swift-lm/MLXLMCommon"
---

# UserInput.Image

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Representation of an image resource.

## Declaration

```swift
struct Image
```

## Topics

### Initializers
- [init(source: Source, label: String?)](./image/init%28source,label%29.md)
### Instance Properties
- [var label: String?](./image/label.md)
  Text that a vision message generator writes into the prompt as `[label]`, immediately before this image. The generator leaves out and logs a label that contains `<`, `>`, `|`, `[` or `]`. A vision processor also leaves out a label whose `[label]` form contains a special token, such as `IMG` on Mistral3.
- [var source: Source](./image/source-swift.property.md)
### Instance Methods
- [func asCIImage() throws -> CIImage](./image/asciimage%28%29.md)
### Type Methods
- [static func array(MLXArray) -> UserInput.Image](./image/array%28_%29.md)
  Makes `arrays.map(UserInput.Image.array)` compile, because a function value cannot use the default `label`.
- [static func array(MLXArray, label: String?) -> UserInput.Image](./image/array%28_,label%29.md)
- [static func ciImage(CIImage) -> UserInput.Image](./image/ciimage%28_%29.md)
  Makes `images.map(UserInput.Image.ciImage)` compile, because a function value cannot use the default `label`.
- [static func ciImage(CIImage, label: String?) -> UserInput.Image](./image/ciimage%28_,label%29.md)
- [static func url(URL) -> UserInput.Image](./image/url%28_%29.md)
  Makes `urls.map(UserInput.Image.url)` compile, because a function value cannot use the default `label`.
- [static func url(URL, label: String?) -> UserInput.Image](./image/url%28_,label%29.md)
### Enumerations
- [UserInput.Image.Source](./image/source-swift.enum.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/userinput/image)*