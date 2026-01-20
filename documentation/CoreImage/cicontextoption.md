# CIContextOption

**Framework**: Core Image  
**Kind**: struct

An enum string type that your code can use to select different options when creating a Core Image context.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct CIContextOption
```

#### Overview

These option keys can be passed to `CIContext` creation APIs such as:

- `/CIContext/contextWithOptions:`
- `/CIContext/contextWithMTLDevice:options:`

## Topics

### Type Properties
- [static let allowLowPower: CIContextOption](cicontextoption/allowlowpower.md)
  A Boolean value to control the power level of Core Image context renders.
- [static let cacheIntermediates: CIContextOption](cicontextoption/cacheintermediates.md)
  A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
- [static let highQualityDownsample: CIContextOption](cicontextoption/highqualitydownsample.md)
  A Boolean value to control the quality of image downsampling operations performed by the Core Image context.
- [static let memoryTarget: CIContextOption](cicontextoption/memorytarget.md)
  A number value to control the maximum memory in megabytes that the context allocates for render tasks.
- [static let name: CIContextOption](cicontextoption/name.md)
  A Boolean value to specify a client-provided name for a context.
- [static let outputColorSpace: CIContextOption](cicontextoption/outputcolorspace.md)
  A Core Image context option key to specify the default destination color space for rendering.
- [static let outputPremultiplied: CIContextOption](cicontextoption/outputpremultiplied.md)
  A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.
- [static let priorityRequestLow: CIContextOption](cicontextoption/priorityrequestlow.md)
  A Boolean value to control the priority Core Image context renders.
- [static let useSoftwareRenderer: CIContextOption](cicontextoption/usesoftwarerenderer.md)
  A Boolean value to control if a Core Image context will use a software renderer.
- [static let workingColorSpace: CIContextOption](cicontextoption/workingcolorspace.md)
  A Core Image context option key to specify the working color space for rendering.
- [static let workingFormat: CIContextOption](cicontextoption/workingformat.md)
  A Core Image context option key to specify the pixel format to for intermediate results when rendering.
- [static let cvMetalTextureCache: CIContextOption](cicontextoption/cvmetaltexturecache.md)
  A Core Video Metal texture cache object to improve the performance of Core Image context renders that use Core Video pixel buffers.
### Initializers
- [init(rawValue: String)](cicontextoption/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption)*