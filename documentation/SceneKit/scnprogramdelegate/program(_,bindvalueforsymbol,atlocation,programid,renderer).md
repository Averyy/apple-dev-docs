# program(_:bindValueForSymbol:atLocation:programID:renderer:)

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Invoked on the delegate to let it bind program values and/or associated graphics resources (such as textures) for symbols.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use the [`handleBinding(ofSymbol:handler:)`](../scnshadable/handlebinding%28ofsymbol,handler%29.md) method of the geometry or material the program is attached to.

## Declaration

```swift
optional func program(_ program: SCNProgram, bindValueForSymbol symbol: String, atLocation location: UInt32, programID: UInt32, renderer: SCNRenderer) -> Bool
```

```objc
- (BOOL) program:(SCNProgram *) program bindValueForSymbol:(NSString *) symbol atLocation:(unsigned int) location programID:(unsigned int) programID renderer:(SCNRenderer *) renderer;
```

## Discussion

If you use the [`handleBinding(ofSymbol:handler:)`](../scnshadable/handlebinding%28ofsymbol,handler%29.md) method to associate a handler block with a SceneKit object for a symbol, SceneKit will not call the delegate’s [`program(_:bindValueForSymbol:atLocation:programID:renderer:)`](./program%28_,bindvalueforsymbol,atlocation,programid,renderer%29.md) method for that symbol when rendering that object.

## Parameters

- `program`: The `SCNProgram` object to bind values for.
- `symbol`: The name of the symbol to bind a value for.
- `location`: The location of the symbol within the program object to be modified.
- `programID`: The underlying OpenGL program object in which the binding is made.
- `renderer`: The renderer that is currently rendering the scene.

## See Also

### Binding and Unbinding Values
- [func program(SCNProgram, unbindValueForSymbol: String, atLocation: UInt32, programID: UInt32, renderer: SCNRenderer)](./program%28_,unbindvalueforsymbol,atlocation,programid,renderer%29.md)
  Invoked on the delegate to let it unbind program values and/or also unbind associated graphic resources (such as textures).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/program(_:bindvalueforsymbol:atlocation:programid:renderer:))*