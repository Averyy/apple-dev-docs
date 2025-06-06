# SCNProgramDelegate

**Framework**: SceneKit  
**Kind**: protocol

The interface for tracking errors that occur when compiling shader source code.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol SCNProgramDelegate : NSObjectProtocol
```

#### Overview

You create and use custom shader programs with the  [`SCNProgram`](scnprogram.md) class.

## Topics

### Handling Shader Compilation Errors
- [func program(SCNProgram, handleError: any Error)](scnprogramdelegate/program(_:handleerror:).md)
  Tells the delegate that an error occurred when compiling GLSL source code.
- [let SCNErrorDomain: String](scnerrordomain.md)
  Identifies an error type defined by the SceneKit framework.
- [SceneKit Error Codes](1409723-scenekit-error-codes.md)
### Finding Fragment Opaqueness
- [func programIsOpaque(SCNProgram) -> Bool](scnprogramdelegate/programisopaque(_:).md)
  Asks the delegate whether fragments rendered by a program are opaque.
### Binding and Unbinding Values
- [func program(SCNProgram, bindValueForSymbol: String, atLocation: UInt32, programID: UInt32, renderer: SCNRenderer) -> Bool](scnprogramdelegate/program(_:bindvalueforsymbol:atlocation:programid:renderer:).md)
  Invoked on the delegate to let it bind program values and/or associated graphics resources (such as textures) for symbols.
- [func program(SCNProgram, unbindValueForSymbol: String, atLocation: UInt32, programID: UInt32, renderer: SCNRenderer)](scnprogramdelegate/program(_:unbindvalueforsymbol:atlocation:programid:renderer:).md)
  Invoked on the delegate to let it unbind program values and/or also unbind associated graphic resources (such as textures).

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any SCNProgramDelegate)?](scnprogram/delegate.md)
  The delegate of the program object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogramdelegate)*