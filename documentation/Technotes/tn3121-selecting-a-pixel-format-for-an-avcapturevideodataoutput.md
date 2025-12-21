# TN3121: Selecting a pixel format for an AVCaptureVideoDataOutput

**Framework**: Technotes

Learn how to choose the best output pixel format for your app.

#### Overview

AVCaptureVideoDataOutput is capable of outputting pixel buffers to your app in many different pixel formats. This Technote will explore the usability and performance characteristics of these formats, enabling you to make an informed decision about the best format to use in your app.

#### Avoid Defaulting to Bgra

A common mistake is to  to selecting ‘BGRA’ as the output format. This format is not a native capture format, which means that AVCapture has to perform a conversion to deliver this format. Additionally, this format requires significantly more memory than many of the native capture formats.

Consider a common scenario where the [`activeFormat`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/activeFormat) of the [`AVCaptureDevice`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice) is configured to capture in ‘420v’:

In this scenario, if you request that the video data output deliver pixel buffers in ‘BGRA’, then AVCapture has to convert every captured ‘420v’ pixel buffer to ‘BGRA’. AVCapture performs these conversions efficiently, but they are not free.

Also, ‘BGRA’ pixel buffers require approximately 2.6x more memory than their ‘420v’ equivalent pixel buffers! This dramatic increase in memory bandwidth usage has serious implications for the efficiency, thermals, and battery consumption of your app.

Instead of paying the costs of pixel format conversion and high memory bandwidth by default, follow the guidance provided in “Choosing the output pixel format” to select an appropriate pixel format for your app.

#### Discovering Available Output Pixel Formats

Not all devices support the full range of output pixel formats. To see the available formats at run time, iterate through the [`AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput)’s array of [`availableVideoPixelFormatTypes`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput/availableVideoPixelFormatTypes).

> **Note**: The availableVideoPixelFormatTypes array is dynamic, and depends on the activeFormat of the capture device that the AVCaptureVideoDataOutput is connected to.

As an example, iPhone 13 Pro supports the following output pixel formats:

| Pixel Format Constant | FourCharCode | Bits Per Channel |
| --- | --- | --- |
| kCVPixelFormatType_420YpCbCr8BiPlanarVideoRange | ‘420v’ | 8 |
| kCVPixelFormatType_Lossless_420YpCbCr8BiPlanarVideoRange | ‘&8v0’ | 8 |
| kCVPixelFormatType_Lossy_420YpCbCr8BiPlanarVideoRange | ‘-8v0’ | 8 |
| kCVPixelFormatType_420YpCbCr8BiPlanarFullRange | ‘420f’ | 8 |
| kCVPixelFormatType_Lossless_420YpCbCr8BiPlanarFullRange | ‘&8f0’ | 8 |
| kCVPixelFormatType_Lossy_420YpCbCr8BiPlanarFullRange | ‘-8f0’ | 8 |
| kCVPixelFormatType_32BGRA | ‘BGRA’ | 8 |
| kCVPixelFormatType_Lossless_32BGRA | ‘&BGA’ | 8 |
| kCVPixelFormatType_Lossy_32BGRA | ‘-BGA’ | 8 |
| kCVPixelFormatType_420YpCbCr10BiPlanarVideoRange | ‘x420’ | 10 |
| kCVPixelFormatType_Lossless_420YpCbCr10PackedBiPlanarVideoRange | ‘&xv0’ | 10 |
| kCVPixelFormatType_Lossy_420YpCbCr10PackedBiPlanarVideoRange | ‘-xv0’ | 10 |
| kCVPixelFormatType_422YpCbCr10BiPlanarVideoRange | ‘x422’ | 10 |
| kCVPixelFormatType_Lossless_422YpCbCr10PackedBiPlanarVideoRange | ‘&xv2’ | 10 |
| kCVPixelFormatType_Lossy_422YpCbCr10PackedBiPlanarVideoRange | ‘-xv2’ | 10 |

#### Choosing the Output Pixel Format

The ideal output pixel format for your app will depend on how your app utilizes the pixel buffers that it receives from the video data output, as well the requirements that you have for your app. There is no exact formula that can be applied to identify this format, but here are a few questions to consider:

- Can your app work with bi-planar YpCbCr pixel buffers, or does it  BGRA pixel buffers?
- Can your app work with compressed pixel buffers, or does it  uncompressed pixel buffers?
- Does your app want to deliver 10-bit high dynamic range content?

Consider the following example scenarios, which are intended to help guide you in selecting the output pixel format for your app:

- Scenario 1: An app takes the output pixel buffers and feeds them to a machine learning model that requires uncompressed BGRA pixel buffers as input. This app is a good candidate for the ‘BGRA’ output pixel format. By specifying this format, this app benefits from efficient conversion from a native capture format to the ‘BGRA’ that is required by the machine learning model.
- Scenario 2: An app takes the output pixel buffers and feeds them to an AVAssetWriter, configured to write with the hevc codec. This app is a good candidate for a bi-planar YpCbCr format, which the asset writer can accept as input. By specifying this format, this app benefits from the efficiency and performance advantages of bi-planar YpCbCr data compared to BGRA data, and if the device this app is running on supports compressed pixel buffer formats, this app can use a compressed variation of the bi-planar format to reduce memory bandwidth even further.
- Scenario 3: An app takes the output pixel buffers and feeds them to a custom Metal kernel to filter that operates on BGRA data. The developer of this app should consider modifying their kernel implementation to operate on bi-planar YCbCr data. Then, the app could request bi-planar YCbCr pixel buffers, greatly reducing its memory bandwidth usage. Since this app’s filter is implemented for the GPU, it can also utilize a compressed variation of its chosen output pixel format on supported devices.

#### Choosing Between Lossy and Lossless

In a scenario where your app can utilize a compressed pixel format, always request the lossy variation as the output pixel format if it is available, which will provide additional memory footprint savings. There is no difference in image quality between the lossy, lossless, and uncompressed pixel buffers that you receive from AVCapture. This is because AVCapture internally uses lossy formats on devices that support them. These lossy formats are implemented such that, for most images, the compression is lossless, while the few remaining images are visually lossless.

#### Revision History

-  First published.

## See Also

- [TN3190: USB audio device design considerations](tn3190-usb-audio-device-design-considerations.md)
  Learn the best techniques for designing devices that conform to the USB Audio Device Class specifications.
- [TN3194: Handling account deletions and revoking tokens for Sign in with Apple](tn3194-handling-account-deletions-and-revoking-tokens-for-sign-in-with-apple.md)
  Learn the best techniques for managing Sign in with Apple user sessions and responding to account deletion requests.
- [TN3193: Managing the on-device foundation model’s context window](tn3193-managing-the-on-device-foundation-model-s-context-window.md)
  Learn how to budget for the context window limit of Apple’s on-device foundation model and handle the error when reaching the limit.
- [TN3115: Bluetooth State Restoration app relaunch rules](tn3115-bluetooth-state-restoration-app-relaunch-rules.md)
  Learn about the conditions under which an iOS app will be relaunched by Bluetooth State Restoration.
- [TN3192: Migrating your iPad app from the deprecated UIRequiresFullScreen key](tn3192-migrating-your-app-from-the-deprecated-uirequiresfullscreen-key.md)
  Support iPad multitasking and dynamic resizing while updating your app to remove the deprecated full-screen compatibility mode.
- [TN3151: Choosing the right networking API](tn3151-choosing-the-right-networking-api.md)
  Learn which networking API is best for you.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3191: IMAP extensions supported by Mail for iOS, iPadOS, and visionOS](tn3191-imap-extensions-supported-by-mail.md)
  Learn which extensions to the RFC 3501 IMAP protocol are supported by Mail for iOS, iPadOS, and visionOS.
- [TN3134: Network Extension provider deployment](tn3134-network-extension-provider-deployment.md)
  Explore the platforms, packaging, OS versions, and device configurations for Network Extension provider deployment.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3121-selecting-a-pixel-format-for-an-avcapturevideodataoutput)*