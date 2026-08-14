# Media Intents

**Framework**: Media Intents  
**Kind**: module

Enable people to use Siri to find and play media from your app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

#### Overview

People use Siri to find and play media from your app. For example, people make specific requests like “Siri, play Example song by Example artist” or “Siri, play the latest episode from $podcast”. However, they also make vague requests, such as “Play the song my friend sent me” or “Play energetic music”. For every request, Siri needs to respond with a matching result from your app.

The Media Intents framework gives your app the [`AudioSearch`](audiosearch.md) type it needs to receive and resolve these requests, regardless of how the person phrases them. The system delivers the app search type to your app using the [`App Intents`](https://developer.apple.com/documentation/appintents) framework, and you use App Intents to return matching results to Siri.

## Topics

### Essentials
- [Responding to audio search and playback requests](responding-to-audio-search-and-playback-requests.md)
  Provide results for audio playback requests that people make by using Siri.
- [struct AudioSearch](audiosearch.md)
  Results and metadata for a person’s audio search and playback request with Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MediaIntents)*