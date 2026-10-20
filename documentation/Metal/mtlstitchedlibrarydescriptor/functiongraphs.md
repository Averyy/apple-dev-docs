# functionGraphs

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The function graphs that define the new stitched library’s functions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var functionGraphs: [MTLFunctionStitchingGraph] { get set }
```

```objc
@property (nonatomic, copy, readwrite, nonnull) NSArray<MTLFunctionStitchingGraph *> * functionGraphs;
```

## See Also

### Configuring a stitched library
- [var functions: [any MTLFunction]](./functions.md)
  The list of functions for creating the stitched library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstitchedlibrarydescriptor/functiongraphs)*