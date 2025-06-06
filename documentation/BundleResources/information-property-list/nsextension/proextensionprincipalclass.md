# ProExtensionPrincipalClass

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the class with the principal implementation of your extension.

**Availability**:
- ProVideo Encoder Extensions 1.0+
- ProVideo Workflow Extensions 1.0+

#### Discussion

The Compressor app instantiates the class specified in the `ProExtensionPrincipalClass` key to convert source files to the output format your extension supports. Customize your extension code by adopting the following protocols in the implementation of this class:

- [`CompressorExtensionSettings`](https://developer.apple.com/documentation/professional_video_applications/CompressorExtensionSettings)
- [`CompressorExtensionColorSpaces`](https://developer.apple.com/documentation/professional_video_applications/CompressorExtensionColorSpaces)
- [`CompressorExtensionSettingsOptional`](https://developer.apple.com/documentation/professional_video_applications/CompressorExtensionSettingsOptional)
- [`CompressorExtensionEncoder`](https://developer.apple.com/documentation/professional_video_applications/CompressorExtensionEncoder)

## See Also

- [ProExtensionAttributes](information-property-list/nsextension/proextensionattributes.md)
  A dictionary that specifies the minimum size of the floating window in which Final Cut Pro hosts the extension view.
- [ProExtensionPrincipalViewControllerClass](information-property-list/nsextension/proextensionprincipalviewcontrollerclass.md)
  The name of the principal view controller class of your extension.
- [ProExtensionUUID](information-property-list/nsextension/proextensionuuid.md)
  A UUID string that uniquely identifies your extension to the Compressor app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/proextensionprincipalclass)*