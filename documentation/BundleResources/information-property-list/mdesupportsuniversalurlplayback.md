# MDESupportsUniversalURLPlayback

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether an app supports URL-based playback via a media device extension.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Details

- **Name**: `MDESupportsUniversalURLPlayback`
- **Type**: boolean

## Discussion

Set this key to `true` in your media app’s `Info.plist` file to turn on the [`AVSystemRoute.LaunchMode.player`](../../AVSystemRouting/avsystemroute-5s2um/launchmode/player.md) launch mode, which uses the remote device’s built-in media player to play a URL:

```xml
<key>MDESupportsUniversalURLPlayback</key>
<true/>
```

When you set this key to `true`, your app can start a playback session using [`AVSystemRouteSession`](../../AVSystemRouting/avsystemroutesession-gp78.md) with a media URL and the [`AVSystemRoute.LaunchMode.player`](../../AVSystemRouting/avsystemroute-5s2um/launchmode/player.md) launch mode. The system routes the URL to the device’s built-in player without requiring a corresponding application on the remote device.

If you don’t set this key to `true`, calls to [`start()`](../../AVSystemRouting/avsystemroutesession-gp78/start%28%29.md) with the [`AVSystemRoute.LaunchMode.player`](../../AVSystemRouting/avsystemroute-5s2um/launchmode/player.md) launch mode fail.

## See Also

### AVSystemRouting
- [MDESupportedProtocols](./mdesupportedprotocols.md)
  A dictionary that declares which media sharing extension protocols an app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/mdesupportsuniversalurlplayback)*