# SCNProgramDelegate

**Framework**: SceneKit  
**Kind**: protocol  
**Role**: Protocol

The interface for tracking errors that occur when compiling shader source code.

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
protocol SCNProgramDelegate : NSObjectProtocol
```

```objc
@protocol SCNProgramDelegate <NSObject>
```

#### Overview

You create and use custom shader programs with the  [`SCNProgram`](./scnprogram.md) class.

## Topics

### Handling Shader Compilation Errors
- [func program(SCNProgram, handleError: any Error)](./scnprogramdelegate/program%28_,handleerror%29.md)
  Tells the delegate that an error occurred when compiling GLSL source code.
- [let SCNErrorDomain: String](./scnerrordomain.md)
  Identifies an error type defined by the SceneKit framework.
- [SceneKit Error Codes](./api-1409723-scenekit-error-codes.md)
### Finding Fragment Opaqueness
- [func programIsOpaque(SCNProgram) -> Bool](./scnprogramdelegate/programisopaque%28_%29.md)
  Asks the delegate whether fragments rendered by a program are opaque.
### Binding and Unbinding Values
- [func program(SCNProgram, bindValueForSymbol: String, atLocation: UInt32, programID: UInt32, renderer: SCNRenderer) -> Bool](./scnprogramdelegate/program%28_,bindvalueforsymbol,atlocation,programid,renderer%29.md)
  Invoked on the delegate to let it bind program values and/or associated graphics resources (such as textures) for symbols.
- [func program(SCNProgram, unbindValueForSymbol: String, atLocation: UInt32, programID: UInt32, renderer: SCNRenderer)](./scnprogramdelegate/program%28_,unbindvalueforsymbol,atlocation,programid,renderer%29.md)
  Invoked on the delegate to let it unbind program values and/or also unbind associated graphic resources (such as textures).

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Providing a Delegate Object
- [var delegate: (any SCNProgramDelegate)?](./scnprogram/delegate.md)
  The delegate of the program object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnprogramdelegate)*