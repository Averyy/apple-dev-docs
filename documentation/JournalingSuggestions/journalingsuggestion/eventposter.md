# JournalingSuggestion.EventPoster

**Framework**: Journaling Suggestions  
**Kind**: struct

A suggestion for a poster image of an event.

**Availability**:
- iOS 26.0+ (Beta)

## Declaration

```swift
struct EventPoster
```

#### Overview

The system provides a `EventPoster` value to your app when a person chooses a suggestion with a event poster

## Topics

### Instance Properties
- [var eventEnd: Date?](journalingsuggestion/eventposter/eventend.md)
  The end date of the event.
- [var eventStart: Date?](journalingsuggestion/eventposter/eventstart.md)
  The start date of the event.
- [var image: URL?](journalingsuggestion/eventposter/image.md)
  A poster image URL.
- [var isHost: Bool?](journalingsuggestion/eventposter/ishost.md)
  Boolean whether the user is the host of the event.
- [var placeName: String?](journalingsuggestion/eventposter/placename.md)
  Location displayed name on the poster.
- [var title: AttributedString](journalingsuggestion/eventposter/title.md)
  The title of the event.
### Type Aliases
- [JournalingSuggestion.EventPoster.JournalingSuggestionContent](journalingsuggestion/eventposter/journalingsuggestioncontent.md)
  Represents a generic content type for journaling suggestions.

## Relationships

### Conforms To
- [JournalingSuggestionAsset](journalingsuggestionasset.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestion/eventposter)*