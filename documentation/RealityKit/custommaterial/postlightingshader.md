# CustomMaterial.PostLightingShader

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+

## Declaration

```swift
struct PostLightingShader
```

## Topics

### Creating a shader
- [init(named: String, in: any MTLLibrary, constantValues: MTLFunctionConstantValues)](custommaterial/postlightingshader/init(named:in:constantvalues:).md)
  Creates a post-lighting shader with the specified function constant values.
### Accessing the Metal library
- [var library: any MTLLibrary](custommaterial/postlightingshader/library.md)
  The Metal library that contains this post-lighting shader function.
### Initializers
- [init(named: String, in: any MTLLibrary)](custommaterial/postlightingshader/init(named:in:).md)
  Creates a post-lighting shader object from a named function in a Metal library.
### Instance Properties
- [var name: String](custommaterial/postlightingshader/name.md)
  The name of the post-lighting shader function.

## Relationships

### Conforms To
- [MaterialFunction](materialfunction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/postlightingshader)*