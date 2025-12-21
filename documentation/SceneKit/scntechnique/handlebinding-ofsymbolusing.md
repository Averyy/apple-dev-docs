# handleBinding(ofSymbol:using:)

**Framework**: SceneKit  
**Kind**: method

Specifies a block to be called before rendering using programs with the specified GLSL uniform variable or attribute name.

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
func handleBinding(ofSymbol symbol: String, using block: SCNBindingBlock? = nil)
```

#### Discussion

This method associates a block for handling setup of an attribute or uniform variable in the shader programs associated with the technique. SceneKit calls your block before any performing any rendering passes that use that symbol. In the block, you can execute any OpenGL commands or other code necessary for preparing your custom shader.

> **Note**:  You must associate a handler block with a technique before assigning that technique to a SceneKit object. The result of calling this method on a technique currently in use is undefined.

Use this method when you need to update a value in a shader program every time SceneKit renders a frame. To set a value infrequently, or only once, use the [`setObject(_:forKeyedSubscript:)`](scntechnique/setobject(_:forkeyedsubscript:).md) or [`setValue(_:forKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/setValue(_:forKey:)) method instead.

If you associate a block with a symbol using this method, SceneKit ignores values set using the [`setObject(_:forKeyedSubscript:)`](scntechnique/setobject(_:forkeyedsubscript:).md) method.

## Parameters

- `symbol`: A GLSL uniform variable or attribute name used in one of the technique’s shader programs.
- `block`: A block that SceneKit calls.

## See Also

- [func setObject(Any?, forKeyedSubscript: any NSCopying)](scntechnique/setobject(_:forkeyedsubscript:).md)
  Sets a value for the specified shader  variable or attribute name, using subscript syntax.
- [subscript(Any) -> Any?](scntechnique/subscript(_:).md)
  Returns the value associated with the specified GLSL uniform variable or attribute name, using subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntechnique/handlebinding(ofsymbol:using:))*