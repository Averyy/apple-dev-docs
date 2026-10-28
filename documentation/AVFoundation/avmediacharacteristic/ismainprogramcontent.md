# isMainProgramContent

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
static let isMainProgramContent: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicIsMainProgramContent;
```

## Discussion

Example: an option that presents the main program audio for the presentation, regardless of locale, would typically have this characteristic.

The value of this characteristic is `public.main-program-content`.

The system infers the presence of this characteristic for a media option; it considers any option that doesn’t have the characteristic [`isAuxiliaryContent`](./isauxiliarycontent.md) to be main content.

## See Also

### Content
- [static let isOriginalContent: AVMediaCharacteristic](./isoriginalcontent.md)
  A media characteristic that indicates that a track or media selection option contains original content.
- [static let isAuxiliaryContent: AVMediaCharacteristic](./isauxiliarycontent.md)
  A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.
- [static let machineGenerated: AVMediaCharacteristic](./machinegenerated.md)
  A media characteristic that indicates that a track was generated in an automated fashion by a machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/ismainprogramcontent)*