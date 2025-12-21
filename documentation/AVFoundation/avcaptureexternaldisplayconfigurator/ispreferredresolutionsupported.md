# isPreferredResolutionSupported

**Framework**: AVFoundation  
**Kind**: property

Whether the external display supports configuration to your preferred resolution.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class var isPreferredResolutionSupported: Bool { get }
```

#### Discussion

If `true`, you may instantiate a configurator with a configuration specifying [`preferredResolution`](avcaptureexternaldisplayconfiguration/preferredresolution.md) set to `true`.

## See Also

- [class var isMatchingFrameRateSupported: Bool](avcaptureexternaldisplayconfigurator/ismatchingframeratesupported.md)
  Whether the external display supports matching frame rate to a capture device.
- [class var isBypassingColorSpaceConversionSupported: Bool](avcaptureexternaldisplayconfigurator/isbypassingcolorspaceconversionsupported.md)
  Whether the external display supports bypassing color space conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/ispreferredresolutionsupported)*