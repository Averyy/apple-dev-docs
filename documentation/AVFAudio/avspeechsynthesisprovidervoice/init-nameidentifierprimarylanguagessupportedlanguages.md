# init(name:identifier:primaryLanguages:supportedLanguages:)

**Framework**: AVFAudio  
**Kind**: init

Creates a voice with a name, an identifier, and language information.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(name: String, identifier: String, primaryLanguages: [String], supportedLanguages: [String])
```

## Parameters

- `name`: The localized name of the voice.
- `identifier`: The unique identifier for the voice.
- `primaryLanguages`: A list of BCP 47 codes that identify the primary languages.
- `supportedLanguages`: A list of BCP 47 codes that identify the languages the voice supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avspeechsynthesisprovidervoice/init(name:identifier:primarylanguages:supportedlanguages:))*