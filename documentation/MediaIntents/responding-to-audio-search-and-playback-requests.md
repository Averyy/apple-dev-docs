# Responding to audio search and playback requests

**Framework**: Media Intents

Provide results for audio playback requests that people make by using Siri.

#### Overview

When a person uses Siri to search your app’s audio catalog, the system needs to query your app for matching content, present results, and allow the person to play content. To integrate your app with Apple Intelligence and Siri and provide this functionality, use the [`App Intents`](https://developer.apple.com/documentation/AppIntents) framework. The Media Intents framework provides the [`AudioSearch`](audiosearch.md) type that you use when searching for matching audio content in your media catalog.

To respond to audio playback requests people make with Siri:

1. Create an *app entity* that describes your app’s audio content and conforms to the entity schemas in the [`Audio`](https://developer.apple.com/documentation/AppIntents/app-schema-domain-audio) domain that App Intents provides. An app entity that conforms to a schema is a lightweight model object that contains the information needed to represent the data in Siri interactions.
2. Implement an [`IntentValueQuery`](https://developer.apple.com/documentation/AppIntents/IntentValueQuery) that finds matching results using the information that [`AudioSearch`](audiosearch.md) provides, and return app entities that represent your playable content.
3. Create an app intent that conforms to the doc://com.apple.documentation/documentation/appintents/assistantschemas/audiointent/playaudio schema and enable Siri to play the audio content.

#### Create App Entities

To return search results to the system, provide audio content in a format that Apple Intelligence and Siri understand by using the App Intents framework. To provide this format, describe audio content by creating an [`AppEntity`](https://developer.apple.com/documentation/AppIntents/AppEntity) that conforms to the matching app entity schema. The [`Audio`](https://developer.apple.com/documentation/AppIntents/app-schema-domain-audio) domain includes entity schemas that represent audio content. For example, if you develop a music player with artists, albums, and songs, create entities that conform to the doc://com.apple.documentation/documentation/appintents/appschemas/audioentity/artist, doc://com.apple.documentation/documentation/appintents/appschemas/audioentity/album, and doc://com.apple.documentation/documentation/appintents/appschemas/audioentity/song schemas.

The following code snippet shows an entity that conforms to the `.audio.song` schema:

```Swift
@AppEntity(schema: .audio.song)
struct SongEntity {
    struct SongEntityQuery: EntityQuery {
        func entities(for identifiers: [SongEntity.ID]) async throws -> [SongEntity] {
            <#code#>
        }
    }
    static let defaultQuery = SongEntityQuery()

    var displayRepresentation: DisplayRepresentation {
        <#DisplayRepresentation#>
    }

    let id: <#Identifiable.ID#>
}
```

To learn more about App Intents and app intent schemas, see [`Apple Intelligence and Siri AI`](https://developer.apple.com/documentation/AppIntents/apple-intelligence-and-siri-ai).

#### Implement the Intent Value Query

When you create an app entity, you include a default query implementation. In the example above, the `SongEntityQuery` structure conforms to [`EntityQuery`](https://developer.apple.com/documentation/AppIntents/EntityQuery), the default protocol you use to provide app entities to the system. To let Siri respond to audio-search and playback requests, extend your entity query to conform to the [`IntentValueQuery`](https://developer.apple.com/documentation/AppIntents/IntentValueQuery) protocol:

```Swift
extension SongEntityQuery: IntentValueQuery {
    func values(for audioSearch: AudioSearch) async throws -> [SongEntity] {
        let foundSongs: [SongEntity]
        
        // Use the audio search information
        // to find matching content.
        foundSongs = try await findMatchingSongs(audioSearch)
        
        return foundSongs
    }
}
```

#### Find Matching Audio Content

People ask Siri to find and play audio content in a variety of ways, from specific requests such as “Siri, play Example song by Example artist” to open-ended asks like “Siri, play energetic music”. As a result, your app’s search logic is particularly important. Use the [`AudioSearch`](audiosearch.md) structure in the [`values(for:)`](https://developer.apple.com/documentation/AppIntents/IntentValueQuery/values(for:)) callback to find matching content and return it as app entities.

The system classifies a person’s request and makes the classification available as the audio search’s [`criteria`](audiosearch/criteria-swift.property.md) property. The following code snippet shows how you might provide recommended content if a person doesn’t include specific information in their request, for example, if a person requests “Play some music”.

```Swift
func findMatchingSongs(_ audioSearch: AudioSearch) async throws -> [SongEntity] {
    switch audioSearch.criteria {
    case .searchQuery(let query):
        // Use the person's utterance to find results.
        // You can use different search strategies.
        return await processSearchQuery(query: query)
    case .unspecified:
        // The person didn't provide specific information; for example,
        // they might say "Play some music". Return relevant results based on
        // their favorites, recommended songs, and so on. 
        return await getRecommendedTracks()
    case .url(let urls):
        // The system was able to provide a URL to specific media.
        // Use it to return results from your catalog.
        return await resolveTracksFromURLs(urls)
    }
}
```

The [`AudioSearch`](audiosearch.md) structure provides you with information based on the system’s understanding of a person’s request:

- **[`AudioSearch.Criteria.searchQuery(_:)`](audiosearch/criteria-swift.enum/searchquery(_:).md)**: The system provides the person’s query, for example, “Example song by Example artist.”
- **[`AudioSearch.Criteria.url(_:)`](audiosearch/criteria-swift.enum/url(_:).md)**: The system was able to identify a URL for the requested audio content. The source for the URL might be a URL that a person includes in their request, or onscreen content that an app made available to the system using the App Intents framework.
- **[`AudioSearch.Criteria.unspecified`](audiosearch/criteria-swift.enum/unspecified.md)**: The person’s request doesn’t include specific information. Return relevant results based on their favorites, recommended songs, and so on.

#### Create the App Intent for the Matching Audio Action

When a person chooses to perform an audio action for the returned results, the system performs your app’s logic for the chosen content. For example, if a person requests a specific song and your intent value query provides a result, the system needs a way to play the song in your app. The App Intents framework lets the system perform audio actions in your app if you implement an app intent that conforms to the schema for the requested action. For example, to allow the system to play a song, create an app intent that conforms to the doc://com.apple.documentation/documentation/appintents/assistantschemas/audiointent/playaudio schema. For more information about implementing an app intent that conforms to a media schema, see [`Audio`](https://developer.apple.com/documentation/AppIntents/app-schema-domain-audio).

## See Also

- [struct AudioSearch](audiosearch.md)
  Results and metadata for a person’s audio search and playback request with Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/responding-to-audio-search-and-playback-requests)*