# setObject(_:forKeyedSubscript:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Sets a value for the specified shader  variable or attribute name, using subscript syntax.

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
func setObject(_ obj: Any?, forKeyedSubscript key: any NSCopying)
```

```objc
- (void) setObject:(id) obj forKeyedSubscript:(id<NSCopying>) key;
```

#### Discussion

The `value` parameter should be an object appropriate to the type of the shader symbol being set. For example, use an [`NSNumber`](../../Foundation/nsnumber.md) object to set the value of a `float` uniform variable, or use an [`NSValue`](../../Foundation/nsvalue.md) object containing an [`SCNVector3`](../scnvector3.md) structure to set the value of a GLSL `vec3` uniform variable or a Metal `float3` variable.

Use this method when you need to set a value infrequently or only once. To update a shader value every time SceneKit renders a frame, use the [`handleBinding(ofSymbol:using:)`](./handlebinding%28ofsymbol,using%29.md) method instead.

If you use the [`handleBinding(ofSymbol:using:)`](./handlebinding%28ofsymbol,using%29.md) method to associate a handler block for a symbol, SceneKit ignores values set for the symbol using the [`setObject(_:forKeyedSubscript:)`](./setobject%28_,forkeyedsubscript%29.md) method.

## Parameters

- `obj`: An object containing a new value for the shader symbol.
- `key`: A shader variable or attribute name used in one of the technique’s shader programs.

## See Also

### Handling Parameters for a Technique’s Shader Programs
- [func handleBinding(ofSymbol: String, using: SCNBindingBlock?)](./handlebinding%28ofsymbol,using%29.md)
  Specifies a block to be called before rendering using programs with the specified GLSL uniform variable or attribute name.
- [subscript(Any) -> Any?](./subscript%28_%29.md)
  Returns the value associated with the specified GLSL uniform variable or attribute name, using subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntechnique/setobject(_:forkeyedsubscript:))*