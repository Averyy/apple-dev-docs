# Video

**Framework**: App Intents  
**Role**: API Collection

Make your video app’s actions available to Apple Intelligence and Siri by adopting schemas for common video playback and watchlist actions.

## Overview

The `.video` domain defines app schemas that provide a structured representation for common video playback actions and content. Apply schemas in the `.video` domain to make your app’s video functionality available to Apple Intelligence and Siri. Each schema defines the requirements for intents, parameters, and results so people get a consistent experience across video apps. For example, a person can play a show with the same phrases on different apps that support the [`playContent`](./appschema/videointent/playcontent.md) schema.

This table maps example phrases that apply to each schema:

| Video intent schemas | Example phrases |
| --- | --- |
| [`playContent`](./appschema/videointent/playcontent.md) | “Play Severance.” or “Watch the Inter Miami match.” |
| [`playTrailer`](./appschema/videointent/playtrailer.md) | “Play the trailer for Silo.” or “Watch the Pluribus trailer.” |
| [`addToWatchList`](./appschema/videointent/addtowatchlist.md) | “Add The Morning Show to my watchlist.” or “Put Shrinking in my up next queue.” |
| [`removeFromWatchList`](./appschema/videointent/removefromwatchlist.md) | “Remove Ted Lasso from my watchlist.” or “Delete Foundation from my up next queue.” |

> 💡 **Tip**: Xcode generates a template implementation when you type `video_` and select a schema from the suggestions list.

For more information about making your app’s actions available to Apple Intelligence and Siri, see [Apple Intelligence and Siri AI](./apple-intelligence-and-siri-ai.md).

## Support video playback use-case groups

A *use-case group* is a set of related schemas that share a single purpose. The use-case group for video playback comprises the [`playContent`](./appschema/videointent/playcontent.md) schema and an [`IntentValueQuery`](./intentvaluequery.md). Your app’s implementation of the query finds video content for playback. Xcode reports a build warning if your app supports one without the other.

> ❗ **Important**: To integrate your app with Apple Intelligence and bring it to Siri AI, adopt both parts of the playback use-case group.

## Topics

### Actions
- [var addToWatchList: some AppSchemaIntent](./appschema/videointent/addtowatchlist.md)
  An intent schema that adds a piece of video content to a person’s watchlist in the TV app.
- [var playContent: some AppSchemaIntent](./appschema/videointent/playcontent.md)
  An intent schema that plays a piece of video content.
- [var playTrailer: some AppSchemaIntent](./appschema/videointent/playtrailer.md)
  An intent schema that plays a trailer for a piece of supported video content.
- [var removeFromWatchList: some AppSchemaIntent](./appschema/videointent/removefromwatchlist.md)
  An intent schema that removes a piece of video content from a person’s watchlist in the TV app.
- [AppSchema.VideoIntent](./appschema/videointent.md)
  Identifies intent schemas in the video domain.
### Content and parameter types
- [var contentCreator: some AppSchemaEntity](./appschema/videoentity/contentcreator.md)
  An entity schema for a content creator.
- [var freeformVideo: some AppSchemaEntity](./appschema/videoentity/freeformvideo.md)
  An entity schema for a freeform video.
- [var image: some AppSchemaEntity](./appschema/videoentity/image.md)
  An entity schema for an image.
- [var movie: some AppSchemaEntity](./appschema/videoentity/movie.md)
  An entity schema for a movie.
- [var person: some AppSchemaEntity](./appschema/videoentity/person.md)
  An entity schema for a person.
- [var tvEpisode: some AppSchemaEntity](./appschema/videoentity/tvepisode.md)
  An entity schema for a tv episode.
- [var tvSeason: some AppSchemaEntity](./appschema/videoentity/tvseason.md)
  An entity schema for a tv season.
- [var tvShow: some AppSchemaEntity](./appschema/videoentity/tvshow.md)
  An entity schema for a tv show.
- [AppSchema.VideoEntity](./appschema/videoentity.md)
  Identifies entity schemas in the video domain.
### Types for static parameters
- [var imageType: some AppSchemaEnum](./appschema/videoenum/imagetype.md)
  An enum schema for an image type parameter.
- [var personRole: some AppSchemaEnum](./appschema/videoenum/personrole.md)
  An enum schema for a person role parameter.
- [var videoContentType: some AppSchemaEnum](./appschema/videoenum/videocontenttype.md)
  An enum schema for a video content type parameter.
- [AppSchema.VideoEnum](./appschema/videoenum.md)
  Identifies enum schemas in the video domain.

## See Also

### Primary domains
- [Audio](./app-schema-domain-audio.md)
  Make your audio app’s actions available to Apple Intelligence and Siri by adopting schemas for common audio playback actions.
- [Calendar](./app-schema-domain-calendar.md)
  Make your calendar app’s actions available to Apple Intelligence and Siri by adopting schemas for common calendar actions.
- [Camera](./app-schema-domain-camera.md)
  Make your camera app’s actions available to Apple Intelligence and Siri by adopting schemas for common camera actions.
- [Clock](./app-schema-domain-clock.md)
  Make your clock app’s actions available to Apple Intelligence and Siri by adopting schemas for common alarm and timer actions.
- [Mail](./app-schema-domain-mail.md)
  Make your email app’s actions available to Apple Intelligence and Siri by adopting schemas for common email actions.
- [Maps](./app-schema-domain-maps.md)
  Make your navigation app’s actions available to Apple Intelligence and Siri by adopting schemas for common navigation actions.
- [Messages](./app-schema-domain-messages.md)
  Make your messaging app’s actions available to Apple Intelligence and Siri by adopting schemas for common messaging actions.
- [Notes](./app-schema-domain-notes.md)
  Make your note-taking app’s actions available to Apple Intelligence and Siri by adopting schemas for common note actions.
- [Phone](./app-schema-domain-phone.md)
  Make your phone app’s actions available to Apple Intelligence and Siri by adopting schemas for calling actions.
- [Photos](./app-schema-domain-photos.md)
  Make your photo and video app’s actions available to Apple Intelligence and Siri by adopting schemas for common photo and video actions.
- [Reminders](./app-schema-domain-reminders.md)
  Make your reminder app’s actions available to Apple Intelligence and Siri by adopting schemas for common reminder actions.
- [System and in-app search](./app-schema-domain-system-and-in-app-search.md)
  Make your app’s actions available to Apple Intelligence and Siri by adopting schemas for in-app search and content access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-schema-domain-video)*