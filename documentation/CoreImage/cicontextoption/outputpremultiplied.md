# outputPremultiplied

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A Boolean value to control how a Core Image context render produces alpha-premultiplied pixels.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static let outputPremultiplied: CIContextOption
```

```c
extern CIContextOption const kCIContextOutputPremultiplied;
```

#### Discussion

This option only affects how a context is rendered when using methods where the destination’s alpha mode cannot be determined such as:

- `/CIContext/render:toBitmap:rowBytes:bounds:format:colorSpace:`
- `/CIContext/render:toCVPixelBuffer:`
- `/CIContext/render:toIOSurface:bounds:colorSpace:`
- `/CIContext/render:toMTLTexture:commandBuffer:bounds:colorSpace:`
- `/CIContext/createCGImage:fromRect:`

If the value for this option is:

- True: The output will produce alpha-premultiplied pixels.
- False: The output will produce un-premultiplied pixels.
- Not specified: the default behavior True.

This option does not affect how a context is rendered to a [`CIRenderDestination`](../cirenderdestination.md) because that API allows you to set or override the alpha behavior using `/CIRenderDestination/alphaMode`.

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
- [static let priorityRequestLow: CIContextOption](./priorityrequestlow.md)
  A Boolean value to control the priority Core Image context renders.
- [static let useSoftwareRenderer: CIContextOption](./usesoftwarerenderer.md)
  A Boolean value to control if a Core Image context will use a software renderer.
- [static let workingColorSpace: CIContextOption](./workingcolorspace.md)
  A Core Image context option key to specify the working color space for rendering.
- [static let workingFormat: CIContextOption](./workingformat.md)
  A Core Image context option key to specify the pixel format to for intermediate results when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/outputpremultiplied)*