# name

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A Boolean value to specify a client-provided name for a context.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static let name: CIContextOption
```

```c
extern CIContextOption const kCIContextName;
```

## Discussion

This name will be used in QuickLook graphs and the output of CI_PRINT_TREE.

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
- [static let outputColorSpace: CIContextOption](./outputcolorspace.md)
  A Core Image context option key to specify the default destination color space for rendering.
- [static let outputPremultiplied: CIContextOption](./outputpremultiplied.md)
  A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [static let priorityRequestLow: CIContextOption](./priorityrequestlow.md)
  A Boolean value to control the priority Core Image context renders.
- [static let useSoftwareRenderer: CIContextOption](./usesoftwarerenderer.md)
  A Boolean value to control if a Core Image context will use a software renderer.
- [static let workingColorSpace: CIContextOption](./workingcolorspace.md)
  A Core Image context option key to specify the working color space for rendering.
- [static let workingFormat: CIContextOption](./workingformat.md)
  A Core Image context option key to specify the pixel format to for intermediate results when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/name)*