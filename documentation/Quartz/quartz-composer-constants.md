# Quartz Composer Constants

**Framework**: Quartz

## Topics

### Constants
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
- [let QCCompositionInputPreviewModeKey: String](qccompositioninputpreviewmodekey.md)
  A Boolean input port whose key is `inputPreviewMode`. When the value of this input port is set to `TRUE`, the composition that provides this port must be able to run in a low-quality mode that produces a preview of the composition.
- [let QCCompositionInputPrimaryColorKey: String](qccompositioninputprimarycolorkey.md)
  A color input port whose key is `inputPrimaryColor`.
- [let QCCompositionInputRSSArticleDurationKey: String](qccompositioninputrssarticledurationkey.md)
  A number input port whose key is `inputRSSArticleDuration`. The value must be expressed in seconds.
- [let QCCompositionInputRSSFeedURLKey: String](qccompositioninputrssfeedurlkey.md)
  A string input port whose key is `inputRSSFeedURL`. This port must be passed an http or feed scheme URL.
- [let QCCompositionInputScreenImageKey: String](qccompositioninputscreenimagekey.md)
  An image input port whose key is `inputScreenImage`.
- [let QCCompositionInputSecondaryColorKey: String](qccompositioninputsecondarycolorkey.md)
  A color input port whose key is `inputSecondaryColor`.
- [let QCCompositionInputSourceImageKey: String](qccompositioninputsourceimagekey.md)
  An  image input port whose key is `inputSourceImage`.
- [let QCCompositionInputTrackInfoKey: String](qccompositioninputtrackinfokey.md)
  A structure input port whose key is `inputTrackInfo`. The structure contains optional entries, such as “name”, “artist”, “album”, “duration”, “artwork”, and so on.
- [let QCCompositionInputTrackPositionKey: String](qccompositioninputtrackpositionkey.md)
  A number input port whose key is `inputTrackPosition`. The value must be expressed in seconds.
- [let QCCompositionInputTrackSignalKey: String](qccompositioninputtracksignalkey.md)
  A Boolean input port whose key is `inputTrackSignal`.
- [let QCCompositionInputXKey: String](qccompositioninputxkey.md)
  A number input port whose key is `inputX`. The value must be normalized to the image width with the origin on the left.
- [let QCCompositionInputYKey: String](qccompositioninputykey.md)
  A number input port whose key is `inputY`. The value must be normalized to the image height with the origin at the bottom.
- [let QCCompositionOutputImageKey: String](qccompositionoutputimagekey.md)
  An image output port whose key is `outputImage`.
- [let QCCompositionOutputWebPageURLKey: String](qccompositionoutputwebpageurlkey.md)
  A string output port whose key is `outputWebPageURL`.
- [let QCCompositionProtocolGraphicAnimation: String](qccompositionprotocolgraphicanimation.md)
  A composition that renders a generic graphical animation. It has the option to use [`QCCompositionInputPrimaryColorKey`](qccompositioninputprimarycolorkey.md) for the primary color of the animation, [`QCCompositionInputSecondaryColorKey`](qccompositioninputsecondarycolorkey.md) for the secondary color of the animation, [`QCCompositionInputPaceKey`](qccompositioninputpacekey.md) for the global pace of the animation, and [`QCCompositionInputPreviewModeKey`](qccompositioninputpreviewmodekey.md) to indicate if the animation should run in lower-quality for preview purposes.
- [let QCCompositionProtocolGraphicTransition: String](qccompositionprotocolgraphictransition.md)
  A  composition that performs a transition between two images, using a transition time in range of `0` to `1`. A conforming composition must use the input keys [`QCCompositionInputSourceImageKey`](qccompositioninputsourceimagekey.md) for the starting image and [`QCCompositionInputDestinationImageKey`](qccompositioninputdestinationimagekey.md) for the image to transition to. The composition can optionally use [`QCCompositionInputPreviewModeKey`](qccompositioninputpreviewmodekey.md) to indicate if the animation should run in lower-quality for preview purposes.
- [let QCCompositionProtocolImageFilter: String](qccompositionprotocolimagefilter.md)
  A  composition that  applies an effect to a source image.  A conforming composition must use the input key [`QCCompositionInputImageKey`](qccompositioninputimagekey.md) for the source image and [`QCCompositionOutputImageKey`](qccompositionoutputimagekey.md) for the output image. The composition can optionally use [`QCCompositionInputXKey`](qccompositioninputxkey.md) to specify the X position of the center point of the effect, [`QCCompositionInputYKey`](qccompositioninputykey.md) to specify the Y position of the center point of the effect, and[`QCCompositionInputPreviewModeKey`](qccompositioninputpreviewmodekey.md) to indicate if the animation should run in lower-quality for preview purposes.
- [let QCCompositionProtocolMusicVisualizer: String](qccompositionprotocolmusicvisualizer.md)
  A  composition that acts as a visualizer for music.  A conforming composition must use the input key [`QCCompositionInputAudioPeakKey`](qccompositioninputaudiopeakkey.md) for the instantaneous audio peak and the [`QCCompositionInputAudioSpectrumKey`](qccompositioninputaudiospectrumkey.md)  for the instantaneous audio spectrum. It can optionally use the [`QCCompositionInputTrackInfoKey`](qccompositioninputtrackinfokey.md) to indicate it receives information about the current  track and the [`QCCompositionInputTrackSignalKey`](qccompositioninputtracksignalkey.md) to indicate the start of a new track.
- [let QCCompositionProtocolRSSVisualizer: String](qccompositionprotocolrssvisualizer.md)
  A  composition that acts as a visualizer for an RSS feed.  A conforming composition must use the input key [`QCCompositionInputRSSFeedURLKey`](qccompositioninputrssfeedurlkey.md) for the URL to use for the RSS feed. It can optionally use [`QCCompositionInputRSSArticleDurationKey`](qccompositioninputrssarticledurationkey.md) to specify the duration of each feed article.
- [let QCCompositionProtocolScreenSaver: String](qccompositionprotocolscreensaver.md)
  A composition that can be used as a screen saver. The composition has the option to use [`QCCompositionInputScreenImageKey`](qccompositioninputscreenimagekey.md) for a screenshot image of the screen that the screen saver runs on, [`QCCompositionInputPreviewModeKey`](qccompositioninputpreviewmodekey.md) to indicate if the animation should run in lower-quality for preview purposes, and [`QCCompositionOutputWebPageURLKey`](qccompositionoutputwebpageurlkey.md) for a  URL to open in the default web browser when screen saver exits (only allowed if screen saver password is disabled).
- [let QCPlugInAttributeCategoriesKey: String](qcpluginattributecategorieskey.md)
- [let QCPlugInAttributeCopyrightKey: String](qcpluginattributecopyrightkey.md)
- [let QCPlugInAttributeDescriptionKey: String](qcpluginattributedescriptionkey.md)
  The key for the custom patch description.
- [let QCPlugInAttributeExamplesKey: String](qcpluginattributeexampleskey.md)
- [let QCPlugInAttributeNameKey: String](qcpluginattributenamekey.md)
  The key for the custom patch name.
- [let QCPlugInExecutionArgumentEventKey: String](qcpluginexecutionargumenteventkey.md)
  The current event.
- [let QCPlugInExecutionArgumentMouseLocationKey: String](qcpluginexecutionargumentmouselocationkey.md)
  The current location of the mouse (as an `NSPoint` object stored in an `NSValue` object) in normalized coordinates relative to the OpenGL context viewport ([0,1]x[0,1] with the origin (`0,0`) at the lower-left corner).
- [let QCPlugInPixelFormatARGB8: String](qcpluginpixelformatargb8.md)
  An ARGB8 format. The alpha component is stored in the most significant bits of each pixel. Each pixel component is 8 bits. For best performance, use this format on PowerPC-based Macintosh computers, as it represents of the order of the data in memory.
- [let QCPlugInPixelFormatBGRA8: String](qcpluginpixelformatbgra8.md)
  A  BGRA8 format. The alpha component is stored in the least significant bits of each pixel. Each pixel component is 8 bits. For best performance, use this format on Intel-PC-based Macintosh computers, as it represents of the order of the data in memory.
- [let QCPlugInPixelFormatI8: String](qcpluginpixelformati8.md)
  An I8 format. Intensity information is represented as an 8-bit value.
- [let QCPlugInPixelFormatIf: String](qcpluginpixelformatif.md)
  An If format. Intensity information is represented as a floating-point value.
- [let QCPlugInPixelFormatRGBAf: String](qcpluginpixelformatrgbaf.md)
  An RGBAf format. Pixel components are represented as floating-point values.
- [let QCPortAttributeDefaultValueKey: String](qcportattributedefaultvaluekey.md)
  The key for the port default value. You can use this key only for value ports (Boolean, Index, Number, Color and String).
- [let QCPortAttributeMaximumValueKey: String](qcportattributemaximumvaluekey.md)
  The key for the port maximum value.
- [let QCPortAttributeMenuItemsKey: String](qcportattributemenuitemskey.md)
  The key for the menu items.
- [let QCPortAttributeMinimumValueKey: String](qcportattributeminimumvaluekey.md)
  The key for the port minimum value.
- [let QCPortAttributeNameKey: String](qcportattributenamekey.md)
  The key for the port name.
- [let QCPortAttributeTypeKey: String](qcportattributetypekey.md)
  The key for the port type. The associated value can be of any of the following constants: [`QCPortTypeBoolean`](qcporttypeboolean.md), [`QCPortTypeIndex`](qcporttypeindex.md), [`QCPortTypeNumber`](qcporttypenumber.md), [`QCPortTypeString`](qcporttypestring.md), [`QCPortTypeColor`](qcporttypecolor.md), [`QCPortTypeImage`](qcporttypeimage.md), or [`QCPortTypeStructure`](qcporttypestructure.md).
- [let QCPortTypeBoolean: String](qcporttypeboolean.md)
  The port type for a Boolean value.
- [let QCPortTypeColor: String](qcporttypecolor.md)
  The port type for a color value.
- [let QCPortTypeImage: String](qcporttypeimage.md)
  The port type for an image.
- [let QCPortTypeIndex: String](qcporttypeindex.md)
  The port type for an index value.
- [let QCPortTypeNumber: String](qcporttypenumber.md)
  The port type for a number value.
- [let QCPortTypeString: String](qcporttypestring.md)
  The port type for a string. The associated value can be an NSString object or any object that responds to the `-stringValue` or `-description` methods.
- [let QCPortTypeStructure: String](qcporttypestructure.md)
  The port type for a collection.
- [let QCRendererEventKey: String](qcrenderereventkey.md)
  A key for a renderer event.
- [let QCRendererMouseLocationKey: String](qcrenderermouselocationkey.md)
  A key for the mouse location.
- [var kQCPlugInExecutionModeConsumer: QCPlugInExecutionMode](kqcpluginexecutionmodeconsumer.md)
  A consumer execution mode. The custom patch always executes assuming the value of its Enable input port is `true`. (The Enable port is automatically added by the system.)
- [var kQCPlugInExecutionModeProcessor: QCPlugInExecutionMode](kqcpluginexecutionmodeprocessor.md)
  A processor execution mode. The custom patch executes whenever its inputs change or if the time change (assuming it’s time-dependent).
- [var kQCPlugInExecutionModeProvider: QCPlugInExecutionMode](kqcpluginexecutionmodeprovider.md)
  A provider execution mode. The custom patch executes on demand—that is, whenever data is requested of it, but at most once per frame.
- [var kQCPlugInTimeModeIdle: QCPlugInTimeMode](kqcplugintimemodeidle.md)
  An idle time dependency. The custom patch does not depend on time but needs the system to execute it periodically. For example if the custom patch connects to a piece of hardware, to ensure that it pulls data from the hardware, you would set the custom patch time dependency to idle time mode. This time mode is  typically used with providers.]]
- [var kQCPlugInTimeModeNone: QCPlugInTimeMode](kqcplugintimemodenone.md)
  No time dependency. The custom patch does not depend on time at all. (It does not use the `time`  parameter of the `execute:atTime:withArguments:` method.)
- [var kQCPlugInTimeModeTimeBase: QCPlugInTimeMode](kqcplugintimemodetimebase.md)
  A time base dependency. The custom patch does depend on time explicitly and has a time base defined by the system. (It uses the `time`  parameter of the `execute:atTime:withArguments:` method.)

## See Also

- [Quartz Data Types](quartz-data-types.md)
- [Quartz Constants](quartz-constants.md)
- [Quartz Enumerations](quartz-enumerations.md)
- [Quartz Composer Enumerations](quartz-composer-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/quartz-composer-constants)*