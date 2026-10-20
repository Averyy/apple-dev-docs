# model(name:part:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Apply to model by `name`, all parts if `part` is nil, otherwise only to the specific `part`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func model(name: String, part: String? = nil) -> MeshScope
```

## See Also

### Creating a mesh scope
- [static func instance(name: String, part: String?) -> MeshScope](./instance%28name,part%29.md)
  Apply to instance by `name`, all parts if `part` is nil, otherwise only to the specific `part`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshscope/model(name:part:))*