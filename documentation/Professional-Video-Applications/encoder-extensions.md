# Encoder Extensions

**Framework**: Professional-Video-Applications  
**Role**: API Collection

Add custom output file formats to the Final Cut Pro workflow.

## Overview

The Compressor app provides a variety of transcoding formats to convert Final Cut Pro source media files into most common media formats. Create encoder extensions to add custom transcoding formats to the Compressor app, allowing Final Cut Pro users to convert their source media files to these output formats.

![Screenshot showing the encoder extension view inside the Compressor interface.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3646161@2x.png)

You create an encoder extension using the Xcode template that comes with the SDK. The SDK has APIs that let you exchange data with the Compressor app and take advantage of Qmaster’s distributed processing service to improve the transcoding time in your extension.

You distribute the encoder extension inside a macOS app. When a user installs the macOS app containing your extension, the extension’s custom file format becomes available in the Compressor app’s Settings interface. Users can then choose your custom transcoding format to encode their Final Cut Pro projects. After encoding the source file into the custom format, the extension writes the encoded output to a user-specified destination.

> ❗ **Important**:  The Compressor SDK is only available for encoder extensions written in Objective-C.

## Topics

### Essentials
- [Building an Encoder Extension](./building-an-encoder-extension.md)
  Create an encoder extension in Xcode by using the Encoder Extension template.
### Information Property List Keys
- [ProExtensionPrincipalClass](../BundleResources/information-property-list/nsextension/proextensionprincipalclass.md)
  The name of the class with the principal implementation of your extension.
- [ProExtensionPrincipalViewControllerClass](../BundleResources/information-property-list/nsextension/proextensionprincipalviewcontrollerclass.md)
  The name of the principal view controller class of your extension.
- [ProExtensionUUID](../BundleResources/information-property-list/nsextension/proextensionuuid.md)
  A UUID string that uniquely identifies your extension to the Compressor app.
### Encoder Extension Settings
- [CompressorExtensionSettings](../professional_video_applications/compressorextensionsettings.md)
  A set of methods you use to manage the extension UI that displays the current encoder settings for users to view and customize.
- [CompressorExtensionColorSpaces](../professional_video_applications/compressorextensioncolorspaces.md)
  An interface you use to specify the supported color spaces in an extension.
### Source Attributes
- [CompressorExtensionSettingsOptional](../professional_video_applications/compressorextensionsettingsoptional.md)
  An interface you use to receive updated values of source media attributes.
### Encoder Attributes
- [Encoder Attributes Settings](./encoder-attributes-settings.md)
  Encoder attributes specify the audio and video configuration values for the output format.
### Source File Decoding
- [CompressorMediaDecoder](../professional_video_applications/compressormediadecoder.md)
  An interface with methods you use to retrieve decoded video, audio, and image data from a source media file.
### Source File Encoding
- [CompressorExtensionEncoder](../professional_video_applications/compressorextensionencoder.md)
  An interface an extension implements to convert source media to the output format supported in your extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/encoder-extensions)*