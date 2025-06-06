# Standard Protocols

**Framework**: Quartz

Protocols for a composition.

## Topics

### Constants
- [let QCCompositionProtocolGraphicAnimation: String](qccompositionprotocolgraphicanimation.md)
  A composition that renders a generic graphical animation. It has the option to use [`QCCompositionInputPrimaryColorKey`](qccompositioninputprimarycolorkey.md) for the primary color of the animation, [`QCCompositionInputSecondaryColorKey`](qccompositioninputsecondarycolorkey.md) for the secondary color of the animation, [`QCCompositionInputPaceKey`](qccompositioninputpacekey.md) for the global pace of the animation, and [`QCCompositionInputPreviewModeKey`](qccompositioninputpreviewmodekey.md) to indicate if the animation should run in lower-quality for preview purposes.
- [let QCCompositionProtocolGraphicTransition: String](qccompositionprotocolgraphictransition.md)
  A  composition that performs a transition between two images, using a transition time in range of `0` to `1`. A conforming composition must use the input keys [`QCCompositionInputSourceImageKey`](qccompositioninputsourceimagekey.md) for the starting image and [`QCCompositionInputDestinationImageKey`](qccompositioninputdestinationimagekey.md) for the image to transition to. The composition can optionally use [`QCCompositionInputPreviewModeKey`](qccompositioninputpreviewmodekey.md) to indicate if the animation should run in lower-quality for preview purposes.
- [let QCCompositionProtocolImageFilter: String](qccompositionprotocolimagefilter.md)
  A  composition that  applies an effect to a source image.  A conforming composition must use the input key [`QCCompositionInputImageKey`](qccompositioninputimagekey.md) for the source image and [`QCCompositionOutputImageKey`](qccompositionoutputimagekey.md) for the output image. The composition can optionally use [`QCCompositionInputXKey`](qccompositioninputxkey.md) to specify the X position of the center point of the effect, [`QCCompositionInputYKey`](qccompositioninputykey.md) to specify the Y position of the center point of the effect, and[`QCCompositionInputPreviewModeKey`](qccompositioninputpreviewmodekey.md) to indicate if the animation should run in lower-quality for preview purposes.
- [let QCCompositionProtocolScreenSaver: String](qccompositionprotocolscreensaver.md)
  A composition that can be used as a screen saver. The composition has the option to use [`QCCompositionInputScreenImageKey`](qccompositioninputscreenimagekey.md) for a screenshot image of the screen that the screen saver runs on, [`QCCompositionInputPreviewModeKey`](qccompositioninputpreviewmodekey.md) to indicate if the animation should run in lower-quality for preview purposes, and [`QCCompositionOutputWebPageURLKey`](qccompositionoutputwebpageurlkey.md) for a  URL to open in the default web browser when screen saver exits (only allowed if screen saver password is disabled).
- [let QCCompositionProtocolRSSVisualizer: String](qccompositionprotocolrssvisualizer.md)
  A  composition that acts as a visualizer for an RSS feed.  A conforming composition must use the input key [`QCCompositionInputRSSFeedURLKey`](qccompositioninputrssfeedurlkey.md) for the URL to use for the RSS feed. It can optionally use [`QCCompositionInputRSSArticleDurationKey`](qccompositioninputrssarticledurationkey.md) to specify the duration of each feed article.
- [let QCCompositionProtocolMusicVisualizer: String](qccompositionprotocolmusicvisualizer.md)
  A  composition that acts as a visualizer for music.  A conforming composition must use the input key [`QCCompositionInputAudioPeakKey`](qccompositioninputaudiopeakkey.md) for the instantaneous audio peak and the [`QCCompositionInputAudioSpectrumKey`](qccompositioninputaudiospectrumkey.md)  for the instantaneous audio spectrum. It can optionally use the [`QCCompositionInputTrackInfoKey`](qccompositioninputtrackinfokey.md) to indicate it receives information about the current  track and the [`QCCompositionInputTrackSignalKey`](qccompositioninputtracksignalkey.md) to indicate the start of a new track.

## See Also

- [Attribute Keys](attribute-keys.md)
  Attributes of a composition.
- [Composition Categories](composition-categories.md)
  Categories for compositions.
- [Standard Protocol Input Keys](standard-protocol-input-keys.md)
  Input ports of a composition.
- [Standard Protocol Output Keys](standard-protocol-output-keys.md)
  Output ports of a composition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/standard-protocols)*