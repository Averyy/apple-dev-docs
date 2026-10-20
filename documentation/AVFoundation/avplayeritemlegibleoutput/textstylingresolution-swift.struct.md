# AVPlayerItemLegibleOutput.TextStylingResolution

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A text styling resolution.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct TextStylingResolution
```

```c
typedef NSString * AVPlayerItemLegibleOutputTextStylingResolution;
```

## Topics

### Text styling options
- [static let `default`: AVPlayerItemLegibleOutput.TextStylingResolution](./textstylingresolution-swift.struct/default.md)
  The text styling information is the same level of information that AVFoundation uses within a player layer.
- [static let sourceAndRulesOnly: AVPlayerItemLegibleOutput.TextStylingResolution](./textstylingresolution-swift.struct/sourceandrulesonly.md)
  The level of resolution excludes styling provided by the user-level Media Accessibility settings.
### Initializers
- [init(rawValue: String)](./textstylingresolution-swift.struct/init%28rawvalue%29.md)
  Creates a text styling resolution structure with a string value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring text styling
- [var textStylingResolution: AVPlayerItemLegibleOutput.TextStylingResolution](./textstylingresolution-swift.property.md)
  A string identifier indicating the degree of text styling to be applied to attributed strings vended by the  object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/textstylingresolution-swift.struct)*