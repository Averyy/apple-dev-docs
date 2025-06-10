# Providing an integrated view of your timeline when playing HLS interstitials

**Framework**: AVFoundation

Go beyond simple ad insertion with point and fill occupancy HLS interstitials.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Xcode 16.0+

#### Overview

> **Note**: This sample code project is associated with WWDC24 session 10114: [`Enhance ad experiences with HLS Interstitials`](https://developer.apple.comhttps://developer.apple.com/wwdc24/10114/)

##### Configure the Sample Code Project

Using the examples under the Live stream examples section of the app requires running a local test stream. The project includes a Go script that starts a local web server that hosts this example stream. You must have [`Go`](https://developer.apple.comhttps://go.dev/doc/install) installed to run this script.

Open a Terminal window, change to the `/Source/LiveStreamExample/` directory, and run the following command to start the stream:

```None
go run liveStreamGenerator.go --http :8443 map.mp4 segment0.m4s segment1.m4s segment2.m4s
```

When the stream starts, copy its URL, which is in the following format: `http://<hostname>:8443/media.m3u8`. In the Xcode project, open the `Menu.json` file, and replace the placeholder URLs (http://livestreamserver.url:8443/media.m3u8) with your local stream URL. Relaunch the app to view the live stream examples.

## See Also

- [class AVPlayerInterstitialEvent](avplayerinterstitialevent.md)
  An object that provides instructions for how a player presents interstitial content.
- [class AVPlayerInterstitialEventController](avplayerinterstitialeventcontroller.md)
  An object that schedules interstitial events for items played by the primary player.
- [class AVPlayerInterstitialEventMonitor](avplayerinterstitialeventmonitor.md)
  An object that monitors the scheduling and progress of interstitial events.
- [class AVPlayerItemIntegratedTimeline](avplayeritemintegratedtimeline.md)
  An object that models the timeline and playback sequence of a primary player item and scheduled interstitial events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/providing-an-integrated-view-of-your-timeline-when-playing-hls-interstitials)*