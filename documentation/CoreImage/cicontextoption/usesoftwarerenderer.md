# useSoftwareRenderer

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A Boolean value to control if a Core Image context will use a software renderer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static let useSoftwareRenderer: CIContextOption
```

```c
extern CIContextOption const kCIContextUseSoftwareRenderer;
```

#### Discussion

> **Note**: This option has no effect if the platform does not support OpenCL.

## See Also

### Type Properties
- [static let allowLowPower: CIContextOption](./allowlowpower.md)
  A Boolean value to control the power level of Core Image context renders.
- [static let cacheIntermediates: CIContextOption](./cacheintermediates.md)
  A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [static let highQualityDownsample: CIContextOption](./highqualitydownsample.md)
  A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [static let memoryTarget: CIContextOption](./memorytarget.md)
  A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [static let name: CIContextOption](./name.md)
  A Boolean value to specify a client-provided name for a context.
- [static let outputColorSpace: CIContextOption](./outputcolorspace.md)
  A Core Image context option key to specify the default destination color space for rendering.
- [static let outputPremultiplied: CIContextOption](./outputpremultiplied.md)
  A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [static let priorityRequestLow: CIContextOption](./priorityrequestlow.md)
  A Boolean value to control the priority Core Image context renders.
- [static let workingColorSpace: CIContextOption](./workingcolorspace.md)
  A Core Image context option key to specify the working color space for rendering.
- [static let workingFormat: CIContextOption](./workingformat.md)
  A Core Image context option key to specify the pixel format to for intermediate results when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/usesoftwarerenderer)*