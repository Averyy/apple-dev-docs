# Audio

**Framework**: App Intents

Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.

#### Overview

The `.audio` domain defines app schemas that provide a structured representation for common audio playback actions and content. Apply schemas in the `.audio` domain to make your app’s audio functionality available to Apple Intelligence and Siri. The [`Media Intents`](https://developer.apple.com/documentation/MediaIntents) framework provides the types that describe a person’s audio search and playback request. Your app implements an [`IntentValueQuery`](intentvaluequery.md) to receive these types, find matching audio content, and return app entities. Each schema defines the requirements for intents, parameters, and results so people get a consistent experience across audio apps. For example, a person can play a song on different apps that support the [`playAudio`](appschema/audiointent/playaudio.md) schema with the same phrases.

The following table maps example phrases that apply to each schema:

| Audio intent schemas | Example phrases |
| --- | --- |
| [`playAudio`](appschema/audiointent/playaudio.md) | “Play music.” or “Play hip-hop in the living room.” |
| [`addToLibrary`](appschema/audiointent/addtolibrary.md) | “Follow this podcast.” or “Add this song to my library.” |
| [`addToPlaylist`](appschema/audiointent/addtoplaylist.md) | “Add this song to my running playlist.” |
| [`createStation`](appschema/audiointent/createstation.md) | “Create a station based on this song.” or “Play more music like this.” |
| [`recognizeAudio`](appschema/audiointent/recognizeaudio.md) | “What song is this?” or “Shazam.” |
| [`updateAudioAffinity`](appschema/audiointent/updateaudioaffinity.md) | “I like this song.” or “I don’t like this song.” |

> 💡 **Tip**: Xcode generates a template implementation when you type `audio_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

## Topics

### Essentials
- [Integrating your music app with Apple Intelligence](integrating-your-music-app-with-apple-intelligence.md)
  Adopt the audio and clock schemas so people can play music and set alarms with Siri.
### Actions
- [var addToLibrary: some AppSchemaIntent](appschema/audiointent/addtolibrary.md)
  An intent schema that adds an audio item to the person’s library.
- [var addToPlaylist: some AppSchemaIntent](appschema/audiointent/addtoplaylist.md)
  An intent schema that adds an audio item to a playlist.
- [var createStation: some AppSchemaIntent](appschema/audiointent/createstation.md)
  An intent schema that starts a station based on the now-playing item.
- [var playAudio: some AppSchemaIntent](appschema/audiointent/playaudio.md)
  An intent schema that plays an audio item.
- [var recognizeAudio: some AppSchemaIntent](appschema/audiointent/recognizeaudio.md)
  An intent schema that finds out what audio is playing nearby.
- [var updateAudioAffinity: some AppSchemaIntent](appschema/audiointent/updateaudioaffinity.md)
  An intent schema that sets the like state of an audio item to liked, unliked, or unset.
- [var warmupAudioQueue: some AppSchemaIntent](appschema/audiointent/warmupaudioqueue.md)
  An intent schema that warms up an audio item by setting the queue without starting playback.
- [AppSchema.AudioIntent](appschema/audiointent.md)
  Identifies intent schemas in the audio domain.
### Content and parameter types
- [var album: some AppSchemaEntity](appschema/audioentity/album.md)
  An entity schema for an album.
- [var algorithmicRadioStation: some AppSchemaEntity](appschema/audioentity/algorithmicradiostation.md)
  An entity schema for an algorithmic radio station.
- [var ambientSound: some AppSchemaEntity](appschema/audioentity/ambientsound.md)
  An entity schema for an ambient sound.
- [var artist: some AppSchemaEntity](appschema/audioentity/artist.md)
  An entity schema for an artist.
- [var audiobook: some AppSchemaEntity](appschema/audioentity/audiobook.md)
  An entity schema for an audiobook.
- [var classicalMusicRecording: some AppSchemaEntity](appschema/audioentity/classicalmusicrecording.md)
  An entity schema for a classical music recording.
- [var liveRadioStation: some AppSchemaEntity](appschema/audioentity/liveradiostation.md)
  An entity schema for a live radio station.
- [var newsBrief: some AppSchemaEntity](appschema/audioentity/newsbrief.md)
  An entity schema for  news brief.
- [var newsProvider: some AppSchemaEntity](appschema/audioentity/newsprovider.md)
  An entity schema for  news provider.
- [var playlist: some AppSchemaEntity](appschema/audioentity/playlist.md)
  An entity schema for a playlist.
- [var podcastCollection: some AppSchemaEntity](appschema/audioentity/podcastcollection.md)
  An entity schema for a podcast collection.
- [var podcastEpisode: some AppSchemaEntity](appschema/audioentity/podcastepisode.md)
  An entity schema for a podcast episode.
- [var podcastShow: some AppSchemaEntity](appschema/audioentity/podcastshow.md)
  An entity schema for a podcast show.
- [var radioShow: some AppSchemaEntity](appschema/audioentity/radioshow.md)
  An entity schema for a radio show.
- [var radioShowEpisode: some AppSchemaEntity](appschema/audioentity/radioshowepisode.md)
  An entity schema for a radio show episode.
- [var song: some AppSchemaEntity](appschema/audioentity/song.md)
  An entity schema for a song.
- [var songCollection: some AppSchemaEntity](appschema/audioentity/songcollection.md)
  An entity schema for a song collection.
- [var warmupAudioQueueResult: some AppSchemaEntity](appschema/audioentity/warmupaudioqueueresult.md)
  An entity schema for a warmup audio queue result.
- [AppSchema.AudioEntity](appschema/audioentity.md)
  Identifies entity schemas in the audio domain.
### Types for static parameters
- [var activity: some AppSchemaEnum](appschema/audioenum/activity.md)
  An enum schema for an activity parameter.
- [var affinityState: some AppSchemaEnum](appschema/audioenum/affinitystate.md)
  An enum schema for an affinity state parameter.
- [var appViewIdentifier: some AppSchemaEnum](appschema/audioenum/appviewidentifier.md)
  An enum schema for an app view identifier parameter.
- [var invocationSource: some AppSchemaEnum](appschema/audioenum/invocationsource.md)
  An enum schema for an invocation source parameter.
- [var playbackAttributes: some AppSchemaEnum](appschema/audioenum/playbackattributes.md)
  An enum schema for a playback attributes parameter.
- [var queueInsertionLocation: some AppSchemaEnum](appschema/audioenum/queueinsertionlocation.md)
  An enum schema for a queue insertion location parameter.
- [AppSchema.AudioEnum](appschema/audioenum.md)
  Identifies enum schemas in the audio domain.

## See Also

- [Calendar](app-schema-domain-calendar.md)
  Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.
- [Camera](app-schema-domain-camera.md)
  Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.
- [Clock](app-schema-domain-clock.md)
  Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.
- [Files](app-schema-domain-files.md)
  Make your file-management app’s actions available to Apple Intelligence and Siri by adopting schemas for common file actions.
- [Mail](app-schema-domain-mail.md)
  Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.
- [Maps](app-schema-domain-maps.md)
  Make your navigation app’s actions available to Apple Intelligence and Siri by adopting schemas for common navigation actions.
- [Messages](app-schema-domain-messages.md)
  Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.
- [Notes](app-schema-domain-notes.md)
  Make your note-taking app’s actions available to Apple Intelligence and Siri by adopting schemas for common note actions.
- [Phone](app-schema-domain-phone.md)
  Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.
- [Photos](app-schema-domain-photos.md)
  Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.
- [Reminders](app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.
- [System and in-app search](app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-audio)*