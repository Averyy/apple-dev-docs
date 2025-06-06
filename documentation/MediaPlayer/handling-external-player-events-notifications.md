# Handling external player events notifications

**Framework**: Media Player

Handle events for external media players.

#### Overview

Apps that play audio or video content receive player events to start and stop playback, change tracks, and even rate an item. All iOS apps that create their own media player, macOS apps, and external media apps should support these events.

> **Note**:  When you use either the system or application player, you don’t get event notifications because those players automatically handle events.

 When you use either the system or application player, you don’t get event notifications because those players automatically handle events.

To receive player event notifications, do the following:

- Use the shared [`MPRemoteCommandCenter`](mpremotecommandcenter.md) object to register handlers for the events you wish to handle and to disable the events you’re not interested to receive.
- Begin playing your content. Your app must be the Now Playing app. An app doesn’t receive remote control events until it begins playing content. Test that your app is properly receiving and handling remote control events with Control Center, which you access by swiping up from the bottom edge of your screen. These controls send remote control events to the app that’s currently or was most recently playing. You can also access the playback controls from the lock screen of the device.

You can ensure that your app interacts well with other apps handling remote control events by following the best practices laid out in the [`Becoming a now playable app`](becoming-a-now-playable-app.md) sample code project.

## See Also

- [Remote command center events](remote-command-center-events.md)
  Set up the remote command center to handle media player events.
- [Track navigation events](track-navigation-events.md)
  Respond to requests to change which part of a media item plays.
- [Media playback mode events](media-playback-mode-events.md)
  Respond to changes in the way media items play.
- [Feedback and rating events](feedback-and-rating-events.md)
  Respond to incoming feedback and rating events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/handling-external-player-events-notifications)*