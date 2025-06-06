# Testing your app’s response to sensitive media

**Framework**: SensitiveContentAnalysis

Trigger your app’s intervention flow by using a special QR code and profile that Apple provides for testing.

#### Overview

You can test your app’s response to nudity in media by analyzing a special QR code. When SensitiveContentAnalysis encounters media that contains the code, the framework flags the media as sensitive. Testing with the QR code enables you to experience your app’s intervention workflow without storing or displaying content that contains nudity. You can use this testing process in an open development environment, or while demonstrating the app to an audience. To enable the framework to recognize the test QR code as sensitive, download and install a special profile on the development device.

##### Download the Qr Code

Although the following image contains no nudity, the framework recognizes it as sensitive content. By returning [`isSensitive`](scsensitivityanalysis/issensitive.md) = `true`, the analyzer ([`SCSensitivityAnalyzer`](scsensitivityanalyzer.md)) returns a false positive for this QR code for the special purpose of testing.

![A QR code.](https://docs-assets.developer.apple.com/published/2ff73e1db185e49d99bb15c77f69e677/testing_your_app_s_response_to_sensitive_media-1%402x.png)

Click or tap to download [`the test image`](https://developer.apple.comhttps://developer.apple.com/sample-code/web/qr-sca.jpg). Use [`the test video`](https://developer.apple.comhttps://developer.apple.com/sample-code/web/qr-sca.mov) to generate a false positive with video.

##### Install the Test Profile

The framework considers the test QR code sensitive only if the development device contains a special profile. Apple provides a special profile specifically for this purpose:

- Download and install the [`SensitiveContentAnalysis profile`](https://developer.apple.comhttps://developer.apple.com/services-account/download?path=/iOS/iOS_Logs/SensitiveContentAnalysis.mobileconfig).
- Reboot the device for the test profile to take effect.

##### Embed the Test Qr Code in Another Image or Video

You can include the QR code in other images or videos, and SensitiveContentAnalysis recognizes the host media as sensitive. For example, you might incorporate the QR code in a larger media file that:

- Indicates the test content with a visual alert such as a yellow triangle
- Brings attention to the test content with an alert in text, such as, “A sensitive image”

If the QR code varies in size or position within the host media, the framework can still recognize it if its details remain crisp and unobstructed. In a video file, position the QR code in the first frame.

##### Test the Media and Generate a False Positive

In your app, check the test media by calling one of the `analyze` functions. For example, call [`analyzeImage(_:completionHandler:)`](scsensitivityanalyzer/analyzeimage(_:completionhandler:).md) and pass in the image as an argument. Or, call [`analyzeVideoFile:completionHandler:`](scsensitivityanalyzer/analyzevideofile:completionhandler:.md) and pass in the test video as an argument. If you have installed the test profile and made it active on your device, the functions return an [`SCSensitivityAnalysis`](scsensitivityanalysis.md) instance with [`isSensitive`](scsensitivityanalysis/issensitive.md) set to `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/testing-your-app-s-response-to-sensitive-media)*