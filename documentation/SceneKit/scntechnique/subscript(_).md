# subscript(_:)

**Framework**: SceneKit  
**Kind**: subscript  
**Role**: Instance Subscript

Returns the value associated with the specified GLSL uniform variable or attribute name, using subscript syntax.

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
subscript(key: Any) -> Any? { get }
```

```objc
- (id) objectForKeyedSubscript:(id) key;
```

## Return Value

An object containing the value of the shader symbol.

## Discussion

This method returns an object appropriate to the type of the shader symbol being set. For example, retrieving the value of a `float` uniform variable returns an [`NSNumber`](../../Foundation/nsnumber.md) object, and retrieving the value of a GLSL `vec3` uniform variable or Metal `float3` variable returns an [`NSValue`](../../Foundation/nsvalue.md) object containing an [`SCNVector3`](../scnvector3.md) structure.

## Parameters

- `key`: A shader variable or attribute name used in one of the technique’s shader programs.

## See Also

### Handling Parameters for a Technique’s Shader Programs
- [func handleBinding(ofSymbol: String, using: SCNBindingBlock?)](./handlebinding%28ofsymbol,using%29.md)
  Specifies a block to be called before rendering using programs with the specified GLSL uniform variable or attribute name.
- [func setObject(Any?, forKeyedSubscript: any NSCopying)](./setobject%28_,forkeyedsubscript%29.md)
  Sets a value for the specified shader  variable or attribute name, using subscript syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntechnique/subscript(_:))*