# AVSystemRouteLaunchMode.application

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

#### Discussion

Use this mode when you want to start your app’s counterpart on the remote device, enabling app-to-application communication and custom playback experiences. The remote application can handle the provided URL and maintain bidirectional communication through the `AVSystemRouteDataChannel` returned in the completion handler.

Application identifiers must be configured in the `MDESupportedProtocols` key in your app’s `Info.plist` file. For example:

```xml
<key>MDESupportedProtocols</key>
<dict>
	<key>com.example.sharingprotocol</key>
	<string>com.example.myapplicationidentifier</string>
</dict>
```

> ❗ **Important**: If `MDESupportedProtocols` is not set, calls to [`startWithCompletionHandler:`](avsystemroutesession-5i6j6/startwithcompletionhandler:.md) fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutelaunchmode/application)*