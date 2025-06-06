# Customizing shaders using function pointers and stitching

**Framework**: Metal

Define custom shader behavior at runtime by creating functions from existing ones and preferentially linking to others in a dynamic library.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- Xcode 13.4+

#### Overview

> **Note**: This sample code project is associated with WWDC2021 session [`10229: Discover compilation workflows in Metal`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10229/) and WWDC2022 session [`6596: Target and optimize GPU binaries with Metal 3`](https://developer.apple.comhttps://developer.apple.com/wwdc22/6596).

This sample code project is associated with WWDC2021 session [`10229: Discover compilation workflows in Metal`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10229/) and WWDC2022 session [`6596: Target and optimize GPU binaries with Metal 3`](https://developer.apple.comhttps://developer.apple.com/wwdc22/6596).

## See Also

- [class MTLStitchedLibraryDescriptor](mtlstitchedlibrarydescriptor.md)
  A description of a new library of procedurally generated functions.
- [class MTLFunctionStitchingGraph](mtlfunctionstitchinggraph.md)
  A description of a new stitched function.
- [class MTLFunctionStitchingInputNode](mtlfunctionstitchinginputnode.md)
  A call graph node that describes an input to the call graph.
- [class MTLFunctionStitchingFunctionNode](mtlfunctionstitchingfunctionnode.md)
  A call graph node that describes a function call and its inputs.
- [protocol MTLFunctionStitchingNode](mtlfunctionstitchingnode.md)
  A protocol to identify call graph nodes.
- [class MTLFunctionStitchingAttributeAlwaysInline](mtlfunctionstitchingattributealwaysinline.md)
  An attribute to specify that Metal needs to inline all of the function calls when generating the stitched function.
- [protocol MTLFunctionStitchingAttribute](mtlfunctionstitchingattribute.md)
  A protocol to identify types that customize how the Metal compiler stitches a function together.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/customizing-shaders-using-function-pointers-and-stitching)*