# MAFlashingLightsProcessor.OptionKey

**Framework**: Media Accessibility  
**Kind**: struct

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

## Topics

### Creating an options structure
- [init(String)](maflashinglightsprocessor/optionkey/init(_:).md)
  Creates an options structure.
- [init(rawValue: String)](maflashinglightsprocessor/optionkey/init(rawvalue:).md)
  Creates an options structure with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func processSurface(IOSurfaceRef, outSurface: inout IOSurfaceRef, timestamp: CFAbsoluteTime, options: [MAFlashingLightsProcessor.OptionKey : Any]?) -> MAFlashingLightsProcessor.Result](maflashinglightsprocessor/processsurface(_:outsurface:timestamp:options:).md)
  Processes a surface by analyzing pixels for sequences of flashing lights and mitigates them by dimming the content.
- [MAFlashingLightsProcessor.Result](maflashinglightsprocessor/result.md)
  An object that reports the result of the flashing lights processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/maflashinglightsprocessor/optionkey)*