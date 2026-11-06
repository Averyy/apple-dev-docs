# playTrailer

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An intent schema that plays a trailer for a piece of supported video content.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var playTrailer: some AppSchemaIntent { get }
```

## Discussion

To make your app’s actions available to Apple Intelligence, conform your [`AppIntent`](../../appintent.md) to a schema that describes your action to the system. If your app’s functionality aligns with the `video` domain and one of your app’s actions matches the `playTrailer` schema, you can generate the properties and protocol conformance the schema requires for your intent implementation with the `@AppIntent( .video.playTrailer)` Swift macro. To make your app work with Siri, see [Apple Intelligence and Siri AI](../../apple-intelligence-and-siri-ai.md).

The following example shows an intent that conforms to the `playTrailer` schema:

```swift
@AppIntent(schema: .video.playTrailer)
struct PlayTrailerIntent {
    /// Content to preview.
    var content: <#TrailerContent#>

    func perform() async throws -> some IntentResult {
        <#code#>
    }
}
```

Define a `@UnionValue` enumeration for the `content` parameter, as in the following example, by typing the first few characters of `video_trailerContent` in Xcode and selecting it from the code-completion suggestions.

```swift
@UnionValue
enum TrailerContent {
    case movie(<#MovieEntity#>)
    case tvShow(<#TVShowEntity#>)
    case tvSeason(<#TVSeasonEntity#>)
}
```

> 💡 **Tip**: Keep the cases that your app supports and remove the rest.

The schema supports the following system experiences:

- Siri
- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Actions
- [var addToWatchList: some AppSchemaIntent](./addtowatchlist.md)
  An intent schema that adds a piece of video content to a person’s watchlist in the TV app.
- [var playContent: some AppSchemaIntent](./playcontent.md)
  An intent schema that plays a piece of video content.
- [var removeFromWatchList: some AppSchemaIntent](./removefromwatchlist.md)
  An intent schema that removes a piece of video content from a person’s watchlist in the TV app.
- [AppSchema.VideoIntent](../videointent.md)
  Identifies intent schemas in the video domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/videointent/playtrailer)*