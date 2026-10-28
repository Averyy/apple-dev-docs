# AudioSearch

**Framework**: Media Intents  
**Kind**: struct  
**Role**: Structure

Results and metadata for a person’s audio search and playback request with Siri.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct AudioSearch
```

## Mentions

- [Responding to audio search and playback requests](./responding-to-audio-search-and-playback-requests.md)

## Overview

People use Apple Intelligence and Siri to find and play audio. By integrating your app’s audio catalog with Apple Intelligence and Siri using the [App Intents](../AppIntents/AppIntents.md) framework, the system forwards search and playback requests to your app, and your app returns audio search results and allows the system to play your app’s songs, podcasts, audiobooks, and so on.

The `AudioSearch` structure captures a person’s audio search and playback request — music, podcasts, audiobooks, or other audio content.

Use `AudioSearch` in your [`IntentValueQuery`](../AppIntents/intentvaluequery.md) implementation to find matching audio content in your app’s media catalog.

For more information about allowing people to find audio content in your app with Apple Intelligence and Siri, see [Responding to audio search and playback requests](./responding-to-audio-search-and-playback-requests.md).

## Topics

### Describing result criteria
- [var criteria: AudioSearch.Criteria](./audiosearch/criteria-swift.property.md)
  The search criteria for the audio request.
- [AudioSearch.Criteria](./audiosearch/criteria-swift.enum.md)
  The metadata and classification of a person’s audio search that the system provides.
### Providing default implementations
- [init(criteria: AudioSearch.Criteria, spotlightSearchResults: [Never])](./audiosearch/init%28criteria,spotlightsearchresults%29.md)
- [static let defaultResolverSpecification: EmptyResolverSpecification<AudioSearch>](./audiosearch/defaultresolverspecification.md)
### Initializers
- [init(criteria: AudioSearch.Criteria)](./audiosearch/init%28criteria%29.md)
  Creates an audio search with a person’s search criteria.
### Type Aliases
- [AudioSearch.Specification](./audiosearch/specification.md)
- [AudioSearch.UnwrappedType](./audiosearch/unwrappedtype.md)
- [AudioSearch.ValueType](./audiosearch/valuetype.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/customlocalizedstringresourceconvertible.md)
- [Decodable](../Swift/decodable.md)
- [DisplayRepresentable](../AppIntents/displayrepresentable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [InstanceDisplayRepresentable](../AppIntents/instancedisplayrepresentable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [PersistentlyIdentifiable](../AppIntents/persistentlyidentifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TypeDisplayRepresentable](../AppIntents/typedisplayrepresentable.md)

## See Also

### Essentials
- [Responding to audio search and playback requests](./responding-to-audio-search-and-playback-requests.md)
  Provide results for audio playback requests that people make by using Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintents/audiosearch)*