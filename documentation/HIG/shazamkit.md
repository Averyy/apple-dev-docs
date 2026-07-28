---
url: https://developer.apple.com/design/human-interface-guidelines/shazamkit
framework: HIG
---

# ShazamKit

**Type:** article

**Platforms:** ios, ipados, macos, tvos, visionos, watchos

ShazamKit supports audio recognition by matching an audio sample against the ShazamKit catalog or a custom audio catalog.

![A sketch of the ShazamKit icon. The image is overlaid with rectangular and circular grid lines and is tinted blue to subtly reflect the blue in the original six-color Apple logo.](https://docs-assets.developer.apple.com/published/b0b4fb8f9584dec4eef88d3dab62402a/technologies-ShazamKit-intro~dark%402x.png)
You can use ShazamKit to provide features like:
- Enhancing experiences with graphics that correspond with the genre of currently playing music
- Making media content accessible to people with hearing disabilities by providing closed captions or sign language that syncs with the audio
- Synchronizing in-app experiences with virtual content in contexts like online learning and retail
If you need the device microphone to get audio samples for your app to recognize, you must request access to it. As with all types of permission requests, it’s important to help people understand why you’re asking for access. For guidance, see [Privacy](privacy.md).
![A screenshot of the Math School app’s permission alert on iPhone. The alert reads 'Math School would like to access your microphone. Synchronize reading and math exercises with videos played by your teacher.' There are two buttons available: Not Now and Allow.](https://docs-assets.developer.apple.com/published/7c24a3b029e6c6df9a1d2c6f8f083f83/shazamkit-mic-permission%402x.png)

## Best practices
After you receive permission to access the microphone for features that use ShazamKit, follow these guidelines.
**Stop recording as soon as possible.** When people allow your app to record audio for recognition, they don’t expect the microphone to stay on. To help preserve privacy, only record for as long as it takes to get the sample you need.
**Let people opt in to storing your app’s recognized songs to their iCloud library.** If your app can store recognized songs to iCloud, give people a way to first approve this action. Even though both the Music Recognition control and the Shazam app show your app as the source of the recognized song, people appreciate having control over which apps can store content in their library.

## Platform considerations
*No additional considerations for iOS, iPadOS, macOS, tvOS, visionOS, or watchOS.*

## Resources

#### Developer documentation
[ShazamKit](../ShazamKit.md)

#### Videos
- [Explore ShazamKit](https://developer.apple.com/videos/play/wwdc2021/10044) - Take advantage of Shazam’s exact audio matching capabilities within your app when you use ShazamKit. Learn how you can harness the immense Shazam catalog to create all sorts of experiences, including quickly recognizing the exact song playing in the background of a video captured by your app, offering dynamic visual effects based on the music playing in a room, or even syncing with external audio to provide companion app experiences. We’ll also show you how you can build custom catalogs within ShazamKit to match with any audio source — all on device.

For a deeper dive, check out “Create custom audio experiences with ShazamKit,” where you’ll code along with us and learn how to build an education app that synchronizes perfectly with streamed video content.



---
*Source: [https://developer.apple.com/design/human-interface-guidelines/shazamkit](https://developer.apple.com/design/human-interface-guidelines/shazamkit)*
