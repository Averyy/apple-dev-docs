# AppSchema.VideoIntent

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies intent schemas in the video domain.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
protocol VideoIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var addToWatchList: some AppSchemaIntent](./videointent/addtowatchlist.md)
  An intent schema that adds a piece of video content to a person’s watchlist in the TV app.
- [var playContent: some AppSchemaIntent](./videointent/playcontent.md)
  An intent schema that plays a piece of video content.
- [var playTrailer: some AppSchemaIntent](./videointent/playtrailer.md)
  An intent schema that plays a trailer for a piece of supported video content.
- [var removeFromWatchList: some AppSchemaIntent](./videointent/removefromwatchlist.md)
  An intent schema that removes a piece of video content from a person’s watchlist in the TV app.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Intent](./intent.md)

## See Also

### Actions
- [var addToWatchList: some AppSchemaIntent](./videointent/addtowatchlist.md)
  An intent schema that adds a piece of video content to a person’s watchlist in the TV app.
- [var playContent: some AppSchemaIntent](./videointent/playcontent.md)
  An intent schema that plays a piece of video content.
- [var playTrailer: some AppSchemaIntent](./videointent/playtrailer.md)
  An intent schema that plays a trailer for a piece of supported video content.
- [var removeFromWatchList: some AppSchemaIntent](./videointent/removefromwatchlist.md)
  An intent schema that removes a piece of video content from a person’s watchlist in the TV app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/videointent)*