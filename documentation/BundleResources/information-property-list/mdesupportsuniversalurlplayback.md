# MDESupportsUniversalURLPlayback

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app supports URL-based playback via a media device extension.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)



**Type**: boolean

#### Discussion

Set this key to `true` in your media app’s `Info.plist` file to turn on the [`AVSystemRoute.LaunchMode.player`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRoute-5s2um/LaunchMode/player) launch mode, which uses the remote device’s built-in media player to play a URL:

```xml
<key>MDESupportsUniversalURLPlayback</key>
<true/>
```

When you set this key to `true`, your app can start a playback session using [`AVSystemRouteSession`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRouteSession-gp78) with a media URL and the [`AVSystemRoute.LaunchMode.player`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRoute-5s2um/LaunchMode/player) launch mode. The system routes the URL to the device’s built-in player without requiring a corresponding application on the remote device.

If you don’t set this key to `true`, calls to [`start()`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRouteSession-gp78/start()) with the [`AVSystemRoute.LaunchMode.player`](https://developer.apple.com/documentation/AVSystemRouting/AVSystemRoute-5s2um/LaunchMode/player) launch mode fail.

## See Also

- [MDESupportedProtocols](information-property-list/mdesupportedprotocols.md)
  A dictionary that declares which media sharing extension protocols an app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/mdesupportsuniversalurlplayback)*