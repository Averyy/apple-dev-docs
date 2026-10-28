# compositionLayerWithFile:

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Creates and returns an instance of a composition layer using the Quartz Composer composition in the specified file.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

## Declaration

```objc
+ (QCCompositionLayer *) compositionLayerWithFile:(NSString *) path;
```

## Return Value

An initialized `QCCompositionLayer` object or `nil` if initialization is not successful.

## Parameters

- `path`: A string that specifies the location of a Quartz Composer composition.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Creating a Composition Layer
- [+ compositionLayerWithComposition:](./compositionlayerwithcomposition_.md)
  Creates and returns an instance of a composition layer using the provided Quartz Composer composition.
- [init!(file: String!)](./init%28file%29.md)
  Initializes and returns a composition layer using the Quartz Composer composition in the specified file.
- [init!(composition: QCComposition!)](./init%28composition%29.md)
  Initializes and returns a  composition layer using the provided Quartz Composer composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionlayer/compositionlayerwithfile:)*