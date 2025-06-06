# Standard Protocol Input Keys

**Framework**: Quartz

Input ports of a composition.

## Topics

### Constants
- [let QCCompositionInputImageKey: String](qccompositioninputimagekey.md)
  An image input port whose key is  `inputImage`.
- [let QCCompositionInputSourceImageKey: String](qccompositioninputsourceimagekey.md)
  An  image input port whose key is `inputSourceImage`.
- [let QCCompositionInputDestinationImageKey: String](qccompositioninputdestinationimagekey.md)
  An image input port whose key is `inputDestinationImage`.
- [let QCCompositionInputRSSFeedURLKey: String](qccompositioninputrssfeedurlkey.md)
  A string input port whose key is `inputRSSFeedURL`. This port must be passed an http or feed scheme URL.
- [let QCCompositionInputRSSArticleDurationKey: String](qccompositioninputrssarticledurationkey.md)
  A number input port whose key is `inputRSSArticleDuration`. The value must be expressed in seconds.
- [let QCCompositionInputPreviewModeKey: String](qccompositioninputpreviewmodekey.md)
  A Boolean input port whose key is `inputPreviewMode`. When the value of this input port is set to `TRUE`, the composition that provides this port must be able to run in a low-quality mode that produces a preview of the composition.
- [let QCCompositionInputXKey: String](qccompositioninputxkey.md)
  A number input port whose key is `inputX`. The value must be normalized to the image width with the origin on the left.
- [let QCCompositionInputYKey: String](qccompositioninputykey.md)
  A number input port whose key is `inputY`. The value must be normalized to the image height with the origin at the bottom.
- [let QCCompositionInputScreenImageKey: String](qccompositioninputscreenimagekey.md)
  An image input port whose key is `inputScreenImage`.
- [let QCCompositionInputAudioPeakKey: String](qccompositioninputaudiopeakkey.md)
  A number input port whose key is `inputAudioPeak`. The value must be in the `[0,1]` range as a mono signal with no decay applied.
- [let QCCompositionInputAudioSpectrumKey: String](qccompositioninputaudiospectrumkey.md)
  A structure input port whose key is `inputAudioSpectrum`. The structure must contain 16 values in the `[0,1]` range representing 16 spectrum bands of the mono signal from low to high frequencies with no decay applied.
- [let QCCompositionInputTrackPositionKey: String](qccompositioninputtrackpositionkey.md)
  A number input port whose key is `inputTrackPosition`. The value must be expressed in seconds.
- [let QCCompositionInputTrackInfoKey: String](qccompositioninputtrackinfokey.md)
  A structure input port whose key is `inputTrackInfo`. The structure contains optional entries, such as “name”, “artist”, “album”, “duration”, “artwork”, and so on.
- [let QCCompositionInputTrackSignalKey: String](qccompositioninputtracksignalkey.md)
  A Boolean input port whose key is `inputTrackSignal`.
- [let QCCompositionInputPrimaryColorKey: String](qccompositioninputprimarycolorkey.md)
  A color input port whose key is `inputPrimaryColor`.
- [let QCCompositionInputSecondaryColorKey: String](qccompositioninputsecondarycolorkey.md)
  A color input port whose key is `inputSecondaryColor`.
- [let QCCompositionInputPaceKey: String](qccompositioninputpacekey.md)
  A number input port whose key is `inputPace`. The value must be in the `[0,1]` range.

## See Also

- [Attribute Keys](attribute-keys.md)
  Attributes of a composition.
- [Composition Categories](composition-categories.md)
  Categories for compositions.
- [Standard Protocol Output Keys](standard-protocol-output-keys.md)
  Output ports of a composition.
- [Standard Protocols](standard-protocols.md)
  Protocols for a composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/standard-protocol-input-keys)*