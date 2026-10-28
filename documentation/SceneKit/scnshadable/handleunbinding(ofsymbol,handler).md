# handleUnbinding(ofSymbol:handler:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Specifies a block to be called after rendering with programs with the specified GLSL uniform variable or attribute name.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
optional func handleUnbinding(ofSymbol symbol: String, handler block: SCNBindingBlock? = nil)
```

```objc
- (void) handleUnbindingOfSymbol:(NSString *) symbol usingBlock:(SCNBindingBlock) block;
```

## Discussion

Use this method to associate a block with a SceneKit object (geometry or material) to handle cleanup related to an attribute or uniform variable in a custom [`SCNProgram`](../scnprogram.md) shader associated with that object. SceneKit will call your block after rendering the object. In the block, you can execute any OpenGL commands or other code necessary for post-rendering tasks.

This method is for OpenGL shader programs only. To bind custom variable data for Metal shader programs, use the [`handleBinding(ofBufferNamed:frequency:handler:)`](../scnprogram/handlebinding%28ofbuffernamed,frequency,handler%29.md) method.

## Parameters

- `symbol`: A GLSL uniform variable or attribute name.
- `block`: A block to be called by SceneKit.

## See Also

### Handling Parameters in Custom OpenGL Shader Programs
- [func handleBinding(ofSymbol: String, handler: SCNBindingBlock?)](./handlebinding%28ofsymbol,handler%29.md)
  Specifies a block to be called before rendering with programs with the specified GLSL uniform variable or attribute name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadable/handleunbinding(ofsymbol:handler:))*