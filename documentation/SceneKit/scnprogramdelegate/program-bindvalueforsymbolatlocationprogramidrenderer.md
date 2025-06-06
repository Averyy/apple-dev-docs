# program(_:bindValueForSymbol:atLocation:programID:renderer:)

**Framework**: SceneKit  
**Kind**: method

Invoked on the delegate to let it bind program values and/or associated graphics resources (such as textures) for symbols.

**Availability**:
- macOS 10.8+

## Declaration

```swift
optional func program(_ program: SCNProgram, bindValueForSymbol symbol: String, atLocation location: UInt32, programID: UInt32, renderer: SCNRenderer) -> Bool
```

#### Discussion

If you use the [`handleBinding(ofSymbol:handler:)`](scnshadable/handlebinding(ofsymbol:handler:).md) method to associate a handler block with a SceneKit object for a symbol, SceneKit will not call the delegate’s [`program(_:bindValueForSymbol:atLocation:programID:renderer:)`](scnprogramdelegate/program(_:bindvalueforsymbol:atlocation:programid:renderer:).md) method for that symbol when rendering that object.

## Parameters

- `program`: The   object to bind values for.
- `symbol`: The name of the symbol to bind a value for.
- `location`: The location of the symbol within the program object to be modified.
- `programID`: The underlying OpenGL program object in which the binding is made.
- `renderer`: The renderer that is currently rendering the scene.

## See Also

- [func program(SCNProgram, unbindValueForSymbol: String, atLocation: UInt32, programID: UInt32, renderer: SCNRenderer)](scnprogramdelegate/program(_:unbindvalueforsymbol:atlocation:programid:renderer:).md)
  Invoked on the delegate to let it unbind program values and/or also unbind associated graphic resources (such as textures).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/program(_:bindvalueforsymbol:atlocation:programid:renderer:))*