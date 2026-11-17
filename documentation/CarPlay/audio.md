# Audio

**Framework**: CarPlay  
**Role**: API Collection

Build an app that plays audio or video content.

## Overview

An audio app plays audio-only content or video and audio together through the CarPlay interface. Create this type of app if your app manages music, podcasts, sports broadcasts, video, or other prerecorded or live-streaming media. In your app’s interface, organize content using lists and other standard elements. When someone selects an item to play, configure the Now Playing interface with the item’s information and show it.

This type of app supports the following CarPlay templates:

- [`CPNowPlayingTemplate`](./cpnowplayingtemplate.md)
- [`CPSearchTemplate`](./cpsearchtemplate.md)
- [`CPTabBarTemplate`](./cptabbartemplate.md)
- [`CPListTemplate`](./cplisttemplate.md)
- [`CPGridTemplate`](./cpgridtemplate.md)
- [`CPVoiceControlTemplate`](./cpvoicecontroltemplate.md)
- [`CPActionSheetTemplate`](./cpactionsheettemplate.md)
- [`CPAlertTemplate`](./cpalerttemplate.md)

> **Note**: CarPlay audio apps also run on Apple HomeView without any modifications.

## Topics

### Essentials
- [CarPlay Audio App](../BundleResources/entitlements/com.apple.developer.carplay-audio.md)
  A Boolean value that indicates whether the CarPlay app plays audio.
- [Integrating CarPlay with Your Music App](./integrating-carplay-with-your-music-app.md)
  Configure your music app to work with CarPlay by displaying a custom UI.
### Playback configuration
- [class CPPlaybackConfiguration](./cpplaybackconfiguration.md)
  Media metadata you add to audio or video items to support automatic system behaviors.
- [protocol CPPlayableItem](./cpplayableitem.md)
  An interface that adds media-based metadata to items with audio or video content.

## See Also

### CarPlay app types
- [Communication](./communication-apps.md)
  Build an app that offers SiriKit messaging or VoIP calling services.
- [Driving task](./driving-task.md)
  Build an app that helps people perform driving-related tasks.
- [EV charging](./ev-charging.md)
  Build an app that provides helpful information about nearby charging facilities.
- [Fueling](./fueling.md)
  Build an app that provides helpful information about nearby fueling stations.
- [Navigation](./navigation-apps.md)
  Build an app that provides turn-by-turn directions to someone while driving.
- [Parking](./parking.md)
  Build an app that provides helpful information about nearby parking facilities.
- [Public safety](./public-safety.md)
  Build an app that offers public safety information to someone who’s driving.
- [Quick food ordering](./quick-food-ordering.md)
  Build an app that helps someone order food for pickup.
- [Video](./video.md)
  Build an app that plays video content exclusively.
- [Voice-based conversation](./voice-based-conversation.md)
  Build an app that responds to questions or requests and performs actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/audio)*