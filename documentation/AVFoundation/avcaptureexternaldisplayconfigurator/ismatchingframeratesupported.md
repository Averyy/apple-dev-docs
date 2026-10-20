# isMatchingFrameRateSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

Whether the external display supports matching frame rate to a capture device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
class var isMatchingFrameRateSupported: Bool { get }
```

```objc
@property (class, readonly, getter=isMatchingFrameRateSupported) BOOL shouldMatchFrameRateSupported;
```

#### Discussion

If `true`, you may instantiate a configurator with a configuration specifying [`shouldMatchFrameRate`](../avcaptureexternaldisplayconfiguration/shouldmatchframerate.md) set to `true`.

## See Also

### Determining configuration support
- [class var isPreferredResolutionSupported: Bool](./ispreferredresolutionsupported.md)
  Whether the external display supports configuration to your preferred resolution.
- [class var isBypassingColorSpaceConversionSupported: Bool](./isbypassingcolorspaceconversionsupported.md)
  Whether the external display supports bypassing color space conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureexternaldisplayconfigurator/ismatchingframeratesupported)*