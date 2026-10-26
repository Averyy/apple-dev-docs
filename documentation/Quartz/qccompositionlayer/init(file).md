# init(file:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Initializes and returns a composition layer using the Quartz Composer composition in the specified file.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
init!(file path: String!)
```

```objc
- (id) initWithFile:(NSString *) path;
```

#### Return Value

The initialized `QCCompositionLayer` object or `nil` if initialization is not successful.

## Parameters

- `path`: A string that specifies the location of a Quartz Composer composition.

## See Also

### Creating a Composition Layer
- [init!(composition: QCComposition!)](./init%28composition%29.md)
  Initializes and returns a  composition layer using the provided Quartz Composer composition.
- [+ compositionLayerWithFile:](./compositionlayerwithfile_.md)
  Creates and returns an instance of a composition layer using the Quartz Composer composition in the specified file.
- [+ compositionLayerWithComposition:](./compositionlayerwithcomposition_.md)
  Creates and returns an instance of a composition layer using the provided Quartz Composer composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionlayer/init(file:))*