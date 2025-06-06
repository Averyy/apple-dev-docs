# TN3145: HDR video metadata

**Framework**: Technotes

Learn about the usage and requirements of “Ambient Viewing Environment” metadata with HLG and / or Dolby Vision™ Profile 8.4 playback.

#### Overview

Starting with iPhone 12, apps can capture, play back, edit and export HDR Video with Dolby Vision.

The normal office or home lighting when using an iPhone indoors is around 314 lux (a measurement of light level intensity). This is significantly different than most of the theatrical movie content graded by professional colorists, which is typically done in a dark room with a 5 nit surround. In order to provide an optimal viewing experience, it’s useful to differentiate between the two types of content for wider viewing conditions. This is especially beneficial when playing back HDR contents on mobile devices where the ambient lighting condition can change dramatically.

> **Note**: A Box in the ISOBMFF (ISO/IEC 14496-12) specification is the same as an Atom in the QuickTime File Format (QTFF). Likewise, a VisualSampleEntry in the ISOBMFF specification is analogous to a video media sample description in the QTFF.

There’s an existing definition in the ISOBMFF (ISO/IEC 14496-12) document:

The AmbientViewingEnvironmentBox box may be used to provide information about the characteristics of the nominal ambient viewing environment for the display of the associated video content and may be present in a VisualSampleEntry. The syntax elements of the ambient viewing environment box may assist the receiving system in adapting the received video content for local display in viewing environments that may be similar or may substantially differ from those assumed or intended when mastering the video content. It is functionally equivalent to, and shall be as described in, the ambient viewing environment SEI message in (ITU-T H.265 |I ISO/IEC 23008-2).

Note: This is a Box, not a FullBox (similar to PixelAspectRatioBox).

```None
class AmbientViewingEnvironmentBox extends Box('amve') { 
    unsigned int(32) ambient_illuminance;
    unsigned int(16) ambient_light_x;
    unsigned int(16) ambient_light_y;
}
```

Semantics for `ambient_illuminance`, `ambient_light_x` and `ambient_light_y` values are in the HVEC (ITU-T H.265 | ISO/IEC 23008-2) document.

#### Dolby Vision Profile 84

iOS 14 and macOS 11 introduced support for Dolby Vision Profile 8.4. Refer to Dolby Vision Streams within the ISOBMFF for the syntax and semantics of the metadata stored within the Dolby Decoder Configuration Record (`'dvvC'`).

##### Constraints on Sample Description Sample Entry

- The codec type shall be `'hvc1'`.
- HEVC shall be encoded at Main10 Profile.
- Dolby Vision Profile 8.4.
- Only Single-track files are supported.
- The Dolby Decoder Configuration Record (`'dvvC'`) shall be present.
- The color (`'colr'`) atom with these values shall be present. - Color Primaries shall be set to 9 (indicating ITU-R BT.2020).
- Color Transfer Function Index shall be set to 18 (indicating ITU-R BT.2100 HLG).
- Color Matrix Index shall be set to 9 (indicating ITU-R BT.2020).
- The ambient viewing environment atom (`'amve'`) shall be present.

![Movie atom with ambient viewing environment atom.](https://docs-assets.developer.apple.com/published/dd2c28425e8303fb8c0d41cbe4740377/tn3145_HDR_video_metadata%402x.png)

#### Capture

Starting with iPhone 12, camera-captured content in Dolby Vision Profile 8.4 and / or HLG format contains the ‘amve’ format description extension in the file (kCMFormatDescriptionExtension_AmbientViewingEnvironment). This is based on ISO/IEC 23008- 2:2017, D.2.39 ambient viewing environment SEI message.

```swift
//Retrieving the ambient viewing environment atom (`'amve'`) from a CMSampleBuffer.
let ambientViewingEnvironment = sampleBuffer.formatDescription?.extensions[.ambentViewingEnvironment]
```

#### Playing Back Hdr Video

Playback using AVPlayer will provide optimal tone mapping on any Apple device. If your application uses `AVSampleBufferDisplayLayer` or `VTDecompressionSession`, you should take extra steps to ensure the `ambientViewingEnvironment` is attached to the `CMSampleBuffer` or `CVPixelBuffer` that are then provided to `enqueueSampleBuffer`.

During playback using `AVSampleBufferDisplayLayer`, the `FormatDescription` attached to the `CMSampleBuffer` may contain the `kCMFormatDescriptionExtension_AmbientViewingEnvironment`.

HDR-rendering applications may check the parameters in the values in the ambient Viewing Environment atoms (`'amve'`) and pick the correct ambient adaptation strategy for their usage cases.

#### Exporting Hdr Video

It is important to preserve the ambient viewing environment metadata during transcoding, as removing this information will result in the video not being displayed correctly on Apple devices due to extra bright imagery. Apple APIs will by default preserve the ambient viewing environment metadata when exporting HDR Video in Dolby Vision Profile 8.4. If you create a new pixel buffer, you need to make sure to take the ambient viewing environment extension from the source and attach it to the new pixel buffer.

#### Incorporating Hdr Video in Your Apps

Refer to [`Incorporating HDR video with Dolby Vision into your apps`](https://developer.apple.comhttps://developer.apple.com/av-foundation/Incorporating-HDR-video-with-Dolby-Vision-into-your-apps.pdf) for additional information on how to safely preview, edit, and export HDR content, as well as how to convert it to SDR.

#### Revision History

-  Clarified support for HLG capture formats. Made other minor editorial changes.
-  First published.

## See Also

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
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Technotes/tn3145-hdr-video-metadata)*