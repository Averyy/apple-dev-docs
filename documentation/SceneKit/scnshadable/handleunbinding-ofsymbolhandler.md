# handleUnbinding(ofSymbol:handler:)

**Framework**: SceneKit  
**Kind**: method

Specifies a block to be called after rendering with programs with the specified GLSL uniform variable or attribute name.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func handleUnbinding(ofSymbol symbol: String, handler block: SCNBindingBlock? = nil)
```

#### Discussion

Use this method to associate a block with a SceneKit object (geometry or material) to handle cleanup related to an attribute or uniform variable in a custom [`SCNProgram`](scnprogram.md) shader associated with that object. SceneKit will call your block after rendering the object. In the block, you can execute any OpenGL commands or other code necessary for post-rendering tasks.

This method is for OpenGL shader programs only. To bind custom variable data for Metal shader programs, use the [`handleBinding(ofBufferNamed:frequency:handler:)`](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md) method.

## Parameters

- `symbol`: A GLSL uniform variable or attribute name.
- `block`: A block to be called by SceneKit.

## See Also

- [func handleBinding(ofSymbol: String, handler: SCNBindingBlock?)](scnshadable/handlebinding(ofsymbol:handler:).md)
  Specifies a block to be called before rendering with programs with the specified GLSL uniform variable or attribute name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadable/handleunbinding(ofsymbol:handler:))*