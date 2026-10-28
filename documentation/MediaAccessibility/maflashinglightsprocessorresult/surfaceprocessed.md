# surfaceProcessed

**Framework**: Media Accessibility  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the flashing lights processor successfully processed the input surface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) BOOL surfaceProcessed;
```

## Discussion

This value is [`false`](../../Swift/false.md) if the flashing lights processor can’t process the surface, which can occur for unsupported hardware or unsupported color spaces.

## See Also

### Interpreting results from video processing
- [intensityLevel](./intensitylevel.md)
  The intensity of flashing lights in the input surface.
- [mitigationLevel](./mitigationlevel.md)
  The amount of mitigation in the output surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessorresult/surfaceprocessed)*