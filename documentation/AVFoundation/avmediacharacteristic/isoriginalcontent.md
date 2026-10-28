# isOriginalContent

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

A media characteristic that indicates that a track or media selection option contains original content.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
static let isOriginalContent: AVMediaCharacteristic
```

```c
extern AVMediaCharacteristic const AVMediaCharacteristicIsOriginalContent;
```

## Discussion

This characteristic differentiates original content from supplementary or derivative content, such as a language translation.

## See Also

### Content
- [static let isMainProgramContent: AVMediaCharacteristic](./ismainprogramcontent.md)
  A media characteristic that indicates a track or media selection option includes content its author indicates is essential to the asset’s presentation.
- [static let isAuxiliaryContent: AVMediaCharacteristic](./isauxiliarycontent.md)
  A media characteristic that indicates a track or media selection option includes content its author indicates is auxiliary to the asset’s presentation.
- [static let machineGenerated: AVMediaCharacteristic](./machinegenerated.md)
  A media characteristic that indicates that a track was generated in an automated fashion by a machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/isoriginalcontent)*