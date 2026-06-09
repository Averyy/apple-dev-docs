# AudioSearch

**Framework**: Media Intents  
**Kind**: struct

Results and metadata for a person’s audio search and playback request with Siri.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AudioSearch
```

## Mentions

- [Responding to audio search and playback requests](responding-to-audio-search-and-playback-requests.md)

#### Overview

People use Apple Intelligence and Siri to find and play audio. By integrating your app’s audio catalog with Apple Intelligence and Siri using the [`App Intents`](https://developer.apple.com/documentation/AppIntents) framework, the system forwards search and playback requests to your app, and your app returns audio search results and allows the system to play your app’s songs, podcasts, audiobooks, and so on.

The `AudioSearch` structure captures a person’s audio search and playback request — music, podcasts, audiobooks, or other audio content — along with any Spotlight results the system finds.

Use `AudioSearch` in your [`IntentValueQuery`](https://developer.apple.com/documentation/AppIntents/IntentValueQuery) implementation to find matching audio content in your app’s media catalog.

For more information about allowing people to find audio content in your app with Apple Intelligence and Siri, see [`Responding to audio search and playback requests`](responding-to-audio-search-and-playback-requests.md).

## Topics

### Describing result criteria
- [var criteria: AudioSearch.Criteria](audiosearch/criteria-swift.property.md)
  The search criteria for the audio request.
- [AudioSearch.Criteria](audiosearch/criteria-swift.enum.md)
  The metadata and classification of a person’s audio search that the system provides.
### Accessing Spotlight search results
- [var spotlightSearchResults: [AudioSearch.SpotlightResult]](audiosearch/spotlightsearchresults.md)
- [AudioSearch.SpotlightResult](audiosearch/spotlightresult.md)
### Providing default implementations
- [init(criteria: AudioSearch.Criteria, spotlightSearchResults: [AudioSearch.SpotlightResult])](audiosearch/init(criteria:spotlightsearchresults:).md)
  Creates an audio search with a person’s search criteria and Spotlight results.
- [static let defaultResolverSpecification: EmptyResolverSpecification<AudioSearch>](audiosearch/defaultresolverspecification.md)
### Type Aliases
- [AudioSearch.Specification](audiosearch/specification.md)
- [AudioSearch.UnwrappedType](audiosearch/unwrappedtype.md)
- [AudioSearch.ValueType](audiosearch/valuetype.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [DisplayRepresentable](../AppIntents/DisplayRepresentable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [InstanceDisplayRepresentable](../AppIntents/InstanceDisplayRepresentable.md)
- [IntentValueConvertible](../AppIntents/IntentValueConvertible.md)
- [IntentValueExpressing](../AppIntents/IntentValueExpressing.md)
- [PersistentlyIdentifiable](../AppIntents/PersistentlyIdentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](../AppIntents/TypeDisplayRepresentable.md)

## See Also

- [Responding to audio search and playback requests](responding-to-audio-search-and-playback-requests.md)
  Provide results for audio playback requests that people make by using Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/audiosearch)*