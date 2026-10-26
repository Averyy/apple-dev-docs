# Media

**Framework**: SiriKit  
**Role**: API Collection

Listen and control audio through Siri Intents, or listen and watch media content from your app with shortcuts.

#### Overview

With the Media domain, users can play and control audio media in your app. Your Intents app extension directs any media-related requests to your app, which then handles the request.

Siri can suggest shortcuts to audio available in your app when the user wants to listen to the content. For example, Siri may suggest a playlist to the user after they connect headphones to their iPhone. These suggestions give the user a convenient way to play the media in your app.

In order for Siri to suggest media content, you should donate an [`INPlayMediaIntent`](https://developer.apple.com/documentation/intents/inplaymediaintent) object to Siri after the user plays the content (see [Donating Shortcuts](./donating-shortcuts.md)). To have Siri suggest new media that might be of interest to the user, save [`INPlayMediaIntent`](https://developer.apple.com/documentation/intents/inplaymediaintent) shortcuts for the new content to the [`INUpcomingMediaManager`](https://developer.apple.com/documentation/intents/inupcomingmediamanager).

## Topics

### Essentials
- [Improving Siri Media Interactions and App Selection](./improving-siri-media-interactions-and-app-selection.md)
  Fine-tune voice controls and improve Siri Suggestions by sharing app capabilities, customized names, and listening habits with the system.
- [Managing Audio with SiriKit](./managing-audio-with-sirikit.md)
  Control audio playback and handle requests to add media using SiriKit Media Intents.
### Playable Media Intents
- [protocol INPlayMediaIntentHandling](https://developer.apple.com/documentation/intents/inplaymediaintenthandling)
  The interface an object implements to confirm and handle play media intents.
- [class INPlayMediaIntent](https://developer.apple.com/documentation/intents/inplaymediaintent)
  An intent that contains information about media playable from your app.
- [class INPlayMediaIntentResponse](https://developer.apple.com/documentation/intents/inplaymediaintentresponse)
  An intents handler’s response to a play media intent.
### Add Media
- [protocol INAddMediaIntentHandling](https://developer.apple.com/documentation/intents/inaddmediaintenthandling)
  The handler interface that adds media.
- [class INAddMediaIntent](https://developer.apple.com/documentation/intents/inaddmediaintent)
  A request to add a media item.
- [class INAddMediaIntentResponse](https://developer.apple.com/documentation/intents/inaddmediaintentresponse)
  An intents handler’s response to an add media intent.
### Search for Media
- [protocol INSearchForMediaIntentHandling](https://developer.apple.com/documentation/intents/insearchformediaintenthandling)
  The interface that handles media search requests.
- [class INSearchForMediaIntent](https://developer.apple.com/documentation/intents/insearchformediaintent)
  A request to search for a media item.
- [class INSearchForMediaIntentResponse](https://developer.apple.com/documentation/intents/insearchformediaintentresponse)
  An intents handler’s response to a search media intent.
### Update Media Affinity
- [protocol INUpdateMediaAffinityIntentHandling](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintenthandling)
  The interface that handles requests to update the user’s preference for a media item.
- [class INUpdateMediaAffinityIntent](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintent)
  A request to update the user’s affinity for a media item.
- [class INUpdateMediaAffinityIntentResponse](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintentresponse)
  An intents handler’s response to an update media affinity intent.
### User Context
- [class INUserContext](https://developer.apple.com/documentation/intents/inusercontext)
  An object that provides user information to Siri.
- [class INMediaUserContext](https://developer.apple.com/documentation/intents/inmediausercontext)
  An object that provides user information to Siri.
### Data Objects
- [class INMediaItem](https://developer.apple.com/documentation/intents/inmediaitem)
  An object that describes a piece of media content, such as a song, TV show, artist, or podcast playlist.
- [class INMediaSearch](https://developer.apple.com/documentation/intents/inmediasearch)
  An object that describes a media type to search for, such as a station name, song name, or album name.
### Upcoming Media
- [class INUpcomingMediaManager](https://developer.apple.com/documentation/intents/inupcomingmediamanager)
  The manager object you use to suggest media to the user.
### Resolution Results
- [class INAddMediaMediaDestinationResolutionResult](https://developer.apple.com/documentation/intents/inaddmediamediadestinationresolutionresult)
  A resolution result for the types of destinations when adding media.
- [class INAddMediaMediaItemResolutionResult](https://developer.apple.com/documentation/intents/inaddmediamediaitemresolutionresult)
  A resolution result for the media item to add.
- [class INMediaDestinationResolutionResult](https://developer.apple.com/documentation/intents/inmediadestinationresolutionresult)
  A resolution result for the media destination types.
- [class INMediaItemResolutionResult](https://developer.apple.com/documentation/intents/inmediaitemresolutionresult)
  A resolution result for media item types.
- [class INMediaAffinityTypeResolutionResult](https://developer.apple.com/documentation/intents/inmediaaffinitytyperesolutionresult)
  A resolution result for the user’s affinity for a media item.
- [class INPlayMediaMediaItemResolutionResult](https://developer.apple.com/documentation/intents/inplaymediamediaitemresolutionresult)
  A resolution result for the media item to play.
- [class INPlayMediaPlaybackSpeedResolutionResult](https://developer.apple.com/documentation/intents/inplaymediaplaybackspeedresolutionresult)
  A resolution result that determines the playback speed of a media item.
- [class INPlaybackRepeatModeResolutionResult](https://developer.apple.com/documentation/intents/inplaybackrepeatmoderesolutionresult)
  A resolution result for the playback repeat modes of a media item.
- [class INPlaybackQueueLocationResolutionResult](https://developer.apple.com/documentation/intents/inplaybackqueuelocationresolutionresult)
  A resolution result for the requested playback queue location.
- [class INSearchForMediaMediaItemResolutionResult](https://developer.apple.com/documentation/intents/insearchformediamediaitemresolutionresult)
  A resolution result for the media item for which to search.
- [class INUpdateMediaAffinityMediaItemResolutionResult](https://developer.apple.com/documentation/intents/inupdatemediaaffinitymediaitemresolutionresult)
  A resolution result for updating the user’s affinity for a media item.

## See Also

### Standard Intents
- [Car Commands](./car-commands.md)
  Manage vehicle door locks and get the vehicle’s status.
- [Lists and Notes](./lists-and-notes.md)
  Create and manage notes and to-do list items.
- [Messaging](./messaging.md)
  Send messages and search the user’s received messages.
- [Payments](./payments.md)
  Send payments between users or pay bills.
- [Restaurant Reservations](./restaurant-reservations.md)
  Create and manage restaurant reservations with help from the Maps app.
- [Ride Booking](./ride-booking.md)
  Book rides and report their status.
- [VoIP Calling](./voip-calling.md)
  Initiate calls and search the user’s call history.
- [Workouts](./workouts.md)
  Start, end, and manage fitness routines.
- [Intent Class Identifiers](./intent-class-identifiers.md)
  Identify intents that user notifications specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikit/media)*