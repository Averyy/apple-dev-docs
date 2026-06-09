# Now Playing

**Framework**: Now Playing  
**Kind**: module

Make your app’s media playback controls available on the Lock Screen, Control Center, and connected accessories.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

#### Overview

The Now Playing framework makes it easy for people to quickly access your app’s media controls across Apple platforms. The Now Playing interface integrates the controls on the Lock Screen, in Control Center, on Apple Watch, and in CarPlay. Use it to publish playback for music, audiobooks, podcasts, movies, TV shows, and other content. You describe your media content and supported commands with an [`Observable`](https://developer.apple.com/documentation/Observation/Observable) model, and the framework updates the system whenever your model changes.

![An illustration of a Now Playing media control card showing track and artist information with play, pause, and skip buttons, surrounded by icons representing iPhone, headphones, a car, a speaker, and Apple Vision Pro.](https://docs-assets.developer.apple.com/published/5817dbb9c02c01618a8f4654ce293274/now-playing-hero%402x.png)

Now Playing supports two kinds of sessions:

- **Local sessions:** Publish playback that happens on the current device. Create a type that conforms to [`MediaSessionRepresentable`](mediasessionrepresentable.md) and use [`MediaSession`](mediasession.md) to register it with the system. The framework observes your [`Observable`](https://developer.apple.com/documentation/Observation/Observable) model and publishes changes to the system as they happen.
- **Remote sessions:** Publish playback that happens on external devices, such as speakers, streaming sticks, or smart TVs. Create an app extension that conforms to [`RemoteMediaSessionExtension`](remotemediasessionextension.md) and provide sessions conforming to [`RemoteMediaSessionRepresentable`](remotemediasessionrepresentable.md). Start remote sessions from your app using [`RemoteMediaSession`](remotemediasession.md), or from your server using push notifications when your app isn’t running.

> ❗ **Important**: Don’t mix the Now Playing framework with the [`MPNowPlayingInfoCenter`](https://developer.apple.com/documentation/MediaPlayer/MPNowPlayingInfoCenter) and [`MPRemoteCommandCenter`](https://developer.apple.com/documentation/MediaPlayer/MPRemoteCommandCenter) APIs from the [`Media Player`](https://developer.apple.com/documentation/MediaPlayer) framework for local playback. Doing so results in undefined behavior.

## Topics

### Local sessions
- [Publishing media sessions](publishing-media-sessions.md)
  Show your app’s media on the Lock Screen and Control Center.
- [protocol MediaSessionRepresentable](mediasessionrepresentable.md)
  A protocol that provides content metadata, playback state, and commands for a Now Playing session.
- [class MediaSession](mediasession.md)
  A local Now Playing session that publishes metadata and commands to the system.
- [enum MediaSessionError](mediasessionerror.md)
  Errors that can occur during local session operations.
### Remote sessions
- [Publishing remote media sessions](publishing-remote-media-sessions.md)
  Show media from an external device on the Lock Screen and Control Center.
- [protocol RemoteMediaSessionRepresentable](remotemediasessionrepresentable.md)
  A session that plays remotely, potentially across multiple devices.
- [class RemoteMediaSession](remotemediasession.md)
  A session that manages remote media playback across devices.
- [protocol RemoteMediaSessionExtension](remotemediasessionextension.md)
  An app extension that provides remote media sessions.
- [class RemoteMediaSessionExtensionConfiguration](remotemediasessionextensionconfiguration.md)
  The configuration object for a remote playback extension.
- [protocol RemoteMediaSessionAttributes](remotemediasessionattributes.md)
  A type that represents attributes for remote sessions.
- [enum RemoteMediaSessionError](remotemediasessionerror.md)
  Errors that can occur during remote session operations.
- [struct MediaDevice](mediadevice.md)
  A device that plays media in a remote session.
### Playback
- [struct MediaPlaybackSnapshot](mediaplaybacksnapshot.md)
  A snapshot of playback state and timing for a Now Playing session.
- [Content types and metadata](content-types-and-metadata.md)
  Describe the media your app is playing.
- [Playback commands](playback-commands.md)
  Declare the playback controls your app supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/NowPlaying)*