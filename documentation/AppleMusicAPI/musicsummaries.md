# MusicSummaries

**Framework**: Apple Music API  
**Kind**: dictionary

The music for the period summary.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object MusicSummaries
```

## Topics

### Dictionaries
- [object MusicSummaries.Attributes](musicsummaries/attributes-data.dictionary.md)
  The attributes for the music summaries resource type.
- [object MusicSummaries.Views](musicsummaries/views-data.dictionary.md)
  The top albums, artists, and songs that the user listened to for the given period.

## Properties

- `attributes` (MusicSummaries.Attributes): The attributes for the music summaries resource type.
- `href` (string) *(required)*: A relative location for the music summaries resource.
- `id` (string) *(required)*: The identifier for the music summaries resource.
- `type` (string) *(required)*: The type of the resource. This value is always `Music Summaries`.
- `views` (MusicSummaries.Views): The views for associations between `Music Summaries` and the user’s top content for that period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/musicsummaries)*