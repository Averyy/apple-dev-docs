# setObject(_:forKeyedSubscript:)

**Framework**: SceneKit  
**Kind**: method

Sets a value for the specified shader  variable or attribute name, using subscript syntax.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setObject(_ obj: Any?, forKeyedSubscript key: any NSCopying)
```

#### Discussion

The `value` parameter should be an object appropriate to the type of the shader symbol being set. For example, use an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object to set the value of a `float` uniform variable, or use an [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object containing an [`SCNVector3`](scnvector3.md) structure to set the value of a GLSL `vec3` uniform variable or a Metal `float3` variable.

Use this method when you need to set a value infrequently or only once. To update a shader value every time SceneKit renders a frame, use the [`handleBinding(ofSymbol:using:)`](scntechnique/handlebinding(ofsymbol:using:).md) method instead.

If you use the [`handleBinding(ofSymbol:using:)`](scntechnique/handlebinding(ofsymbol:using:).md) method to associate a handler block for a symbol, SceneKit ignores values set for the symbol using the [`setObject(_:forKeyedSubscript:)`](scntechnique/setobject(_:forkeyedsubscript:).md) method.

## Parameters

- `obj`: An object containing a new value for the shader symbol.
- `key`: A shader variable or attribute name used in one of the technique’s shader programs.

## See Also

- [func handleBinding(ofSymbol: String, using: SCNBindingBlock?)](scntechnique/handlebinding(ofsymbol:using:).md)
  Specifies a block to be called before rendering using programs with the specified GLSL uniform variable or attribute name.
- [subscript(Any) -> Any?](scntechnique/subscript(_:).md)
  Returns the value associated with the specified GLSL uniform variable or attribute name, using subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntechnique/setobject(_:forkeyedsubscript:))*