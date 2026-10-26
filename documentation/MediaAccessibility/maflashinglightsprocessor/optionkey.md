# MAFlashingLightsProcessor.OptionKey

**Framework**: Media Accessibility  
**Kind**: struct  
**Role**: Structure

Options for the flashing lights processor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 13.0+
- macOS 10.9+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct OptionKey
```

```c
typedef NSString * MAFlashingLightsProcessorOptionKey;
```

## Topics

### Creating an options structure
- [init(String)](./optionkey/init%28_%29.md)
  Creates an options structure.
- [init(rawValue: String)](./optionkey/init%28rawvalue%29.md)
  Creates an options structure with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Processing video content
- [func processSurface(IOSurfaceRef, outSurface: inout IOSurfaceRef, timestamp: CFAbsoluteTime, options: [MAFlashingLightsProcessor.OptionKey : Any]?) -> MAFlashingLightsProcessor.Result](./processsurface%28_,outsurface,timestamp,options%29.md)
  Processes a surface by analyzing pixels for sequences of flashing lights and mitigates them by dimming the content.
- [MAFlashingLightsProcessor.Result](./result.md)
  An object that reports the result of the flashing lights processor.
- [- processSurface:outSurface:timestamp:options:](./processsurface_outsurface_timestamp_options_.md)
  Processes a surface by analyzing pixels for sequences of flashing lights and mitigates them by dimming the content.
- [MAFlashingLightsProcessorResult](../maflashinglightsprocessorresult.md)
  An object that reports the result of the flashing lights processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/optionkey)*