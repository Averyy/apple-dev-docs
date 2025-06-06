# QCPortTypeStructure

**Framework**: Quartz  
**Kind**: var

The port type for a collection.

**Availability**:
- macOS 10.4+

## Declaration

```swift
let QCPortTypeStructure: String
```

## See Also

- [let QCCompositionAttributeBuiltInKey: String](qccompositionattributebuiltinkey.md)
  The key for the composition origin.
- [let QCCompositionAttributeCategoryKey: String](qccompositionattributecategorykey.md)
  A key representing a composition category.
- [let QCCompositionAttributeCopyrightKey: String](qccompositionattributecopyrightkey.md)
  The key for composition copyright information. The associated value is an `NSString` object.
- [let QCCompositionAttributeDescriptionKey: String](qccompositionattributedescriptionkey.md)
  The key for the composition description. The associated value is an `NSString` object.
- [let QCCompositionAttributeHasConsumersKey: String](qccompositionattributehasconsumerskey.md)
  The key for a composition that has consumer patches.
- [let QCCompositionAttributeIsTimeDependentKey: String](qccompositionattributeistimedependentkey.md)
- [let QCCompositionAttributeNameKey: String](qccompositionattributenamekey.md)
  The key for the composition name. The associated value is an `NSString` object.
- [let QCCompositionCategoryDistortion: String](qccompositioncategorydistortion.md)
  A composition that produces a distortion effect.
- [let QCCompositionCategoryStylize: String](qccompositioncategorystylize.md)
  A composition that produces a stylize effect.
- [let QCCompositionCategoryUtility: String](qccompositioncategoryutility.md)
  A utility composition.
- [let QCCompositionInputAudioPeakKey: String](qccompositioninputaudiopeakkey.md)
  A number input port whose key is `inputAudioPeak`. The value must be in the `[0,1]` range as a mono signal with no decay applied.
- [let QCCompositionInputAudioSpectrumKey: String](qccompositioninputaudiospectrumkey.md)
  A structure input port whose key is `inputAudioSpectrum`. The structure must contain 16 values in the `[0,1]` range representing 16 spectrum bands of the mono signal from low to high frequencies with no decay applied.
- [let QCCompositionInputDestinationImageKey: String](qccompositioninputdestinationimagekey.md)
  An image input port whose key is `inputDestinationImage`.
- [let QCCompositionInputImageKey: String](qccompositioninputimagekey.md)
  An image input port whose key is  `inputImage`.
- [let QCCompositionInputPaceKey: String](qccompositioninputpacekey.md)
  A number input port whose key is `inputPace`. The value must be in the `[0,1]` range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcporttypestructure)*