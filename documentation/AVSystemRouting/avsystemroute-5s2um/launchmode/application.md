# AVSystemRoute.LaunchMode.application

**Framework**: AVSystemRouting  
**Kind**: case

Launches the corresponding application on the remote device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
case application
```

## Mentions

- [Routing and streaming media to remote devices](routing-and-streaming-media-to-remote-devices.md)
- [Routing media to third-party devices](routing-media-to-third-party-devices.md)

#### Discussion

Use this mode when you want to start your app’s counterpart on the remote device, enabling app-to-application communication and custom playback experiences. The remote application can handle the provided URL and maintain bidirectional communication through the [`AVSystemRoute.DataChannel`](avsystemroute-5s2um/datachannel.md) returned by [`start()`](avsystemroutesession-gp78/start().md).

Application identifiers must be configured in the `MDESupportedProtocols` key in your app’s `Info.plist` file. For example:

```xml
<key>MDESupportedProtocols</key>
<dict>
	<key>com.example.sharingprotocol</key>
	<string>com.example.myapplicationidentifier</string>
</dict>
```

> ❗ **Important**: If `MDESupportedProtocols` is not set, calls to [`start()`](avsystemroutesession-gp78/start().md) fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-5s2um/launchmode/application)*