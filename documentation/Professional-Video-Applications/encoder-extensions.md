# Encoder Extensions

**Framework**: Professional-Video-Applications  
**Role**: API Collection

Add custom output file formats to the Final Cut Pro workflow.

#### Overview

The Compressor app provides a variety of transcoding formats to convert Final Cut Pro source media files into most common media formats. Create encoder extensions to add custom transcoding formats to the Compressor app, allowing Final Cut Pro users to convert their source media files to these output formats.

![Screenshot showing the encoder extension view inside the Compressor interface.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3646161@2x.png)

You create an encoder extension using the Xcode template that comes with the SDK. The SDK has APIs that let you exchange data with the Compressor app and take advantage of Qmaster’s distributed processing service to improve the transcoding time in your extension.

You distribute the encoder extension inside a macOS app. When a user installs the macOS app containing your extension, the extension’s custom file format becomes available in the Compressor app’s Settings interface. Users can then choose your custom transcoding format to encode their Final Cut Pro projects. After encoding the source file into the custom format, the extension writes the encoded output to a user-specified destination.

> ❗ **Important**:  The Compressor SDK is only available for encoder extensions written in Objective-C.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/encoder-extensions)*