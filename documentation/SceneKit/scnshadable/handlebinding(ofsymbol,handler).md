# handleBinding(ofSymbol:handler:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Specifies a block to be called before rendering with programs with the specified GLSL uniform variable or attribute name.

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
optional func handleBinding(ofSymbol symbol: String, handler block: SCNBindingBlock? = nil)
```

```objc
- (void) handleBindingOfSymbol:(NSString *) symbol usingBlock:(SCNBindingBlock) block;
```

## Discussion

Use this method to associate a block with a SceneKit object (geometry or material) to handle setup of an attribute or uniform variable in a custom [`SCNProgram`](../scnprogram.md) shader associated with that object. SceneKit calls your block before rendering the object. In the block, you can execute any OpenGL commands or other code necessary for preparing your custom shader. For example, the following block updates the `time` uniform variable in a custom fragment shader for producing animated effects:

```objc
CFTimeInterval startTime = CFAbsoluteTimeGetCurrent();
[myNode.geometry.firstMaterial handleBindingOfSymbol:@"time" usingBlock:
    ^(unsigned int programID, unsigned int location, SCNNode *renderedNode, SCNRenderer *renderer) {
        glUniform1f(location, CFAbsoluteTimeGetCurrent() - startTime);
    }];
```

This method is for OpenGL shader programs only. To bind custom variable data for Metal shader programs, use the [`handleBinding(ofBufferNamed:frequency:handler:)`](../scnprogram/handlebinding%28ofbuffernamed,frequency,handler%29.md) method.

## Parameters

- `symbol`: A GLSL uniform variable or attribute name.
- `block`: A block to be called by SceneKit.

## See Also

### Handling Parameters in Custom OpenGL Shader Programs
- [func handleUnbinding(ofSymbol: String, handler: SCNBindingBlock?)](./handleunbinding%28ofsymbol,handler%29.md)
  Specifies a block to be called after rendering with programs with the specified GLSL uniform variable or attribute name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshadable/handlebinding(ofsymbol:handler:))*