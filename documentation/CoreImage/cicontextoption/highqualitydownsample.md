# highQualityDownsample

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A Boolean value to control the quality of image downsampling operations performed by the Core Image context.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let highQualityDownsample: CIContextOption
```

```c
extern CIContextOption const kCIContextHighQualityDownsample;
```

## Discussion

The higher quality behavior performs downsampling operations in multiple passes in order to reduce aliasing artifacts.

The lower quality behavior performs downsampling operations a single pass in order to improve performance.

If the value for this option is:

- True: The higher quality behavior will be used.
- False: The lower quality behavior will be used.
- Not specified: the default behavior is True on macOS and False on other platforms.

> **Note**:
>
> - This option does affect how `/CIImage/imageByApplyingTransform:` operations are performed by the context.
> - This option does not affect how `/CIImage/imageByApplyingTransform:highQualityDownsample:` behaves.

## See Also

### Type Properties
- [static let allowLowPower: CIContextOption](./allowlowpower.md)
  A Boolean value to control the power level of Core Image context renders.
- [static let cacheIntermediates: CIContextOption](./cacheintermediates.md)
  A Boolean value to control how a Core Image context caches the contents of any intermediate image buffers it uses during rendering.
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
- [static let useSoftwareRenderer: CIContextOption](./usesoftwarerenderer.md)
  A Boolean value to control if a Core Image context will use a software renderer.
- [static let workingColorSpace: CIContextOption](./workingcolorspace.md)
  A Core Image context option key to specify the working color space for rendering.
- [static let workingFormat: CIContextOption](./workingformat.md)
  A Core Image context option key to specify the pixel format to for intermediate results when rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontextoption/highqualitydownsample)*