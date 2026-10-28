# compositionLayerWithComposition:

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Creates and returns an instance of a composition layer using the provided Quartz Composer composition.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

## Declaration

```objc
+ (QCCompositionLayer *) compositionLayerWithComposition:(QCComposition *) composition;
```

## Return Value

An initialized `QCCompositionLayer` object or `nil` if initialization is not successful.

## Parameters

- `composition`: The Quartz Composer composition to use as content.

## See Also

### Creating a Composition Layer
- [+ compositionLayerWithFile:](./compositionlayerwithfile_.md)
  Creates and returns an instance of a composition layer using the Quartz Composer composition in the specified file.
- [init!(file: String!)](./init%28file%29.md)
  Initializes and returns a composition layer using the Quartz Composer composition in the specified file.
- [init!(composition: QCComposition!)](./init%28composition%29.md)
  Initializes and returns a  composition layer using the provided Quartz Composer composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionlayer/compositionlayerwithcomposition:)*