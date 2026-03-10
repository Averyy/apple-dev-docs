# attributedSourceText

**Framework**: Translation  
**Kind**: property

The text to translate, including styling like bold text, italics, and hyperlink data for linking between data sources.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)

## Declaration

```swift
var attributedSourceText: AttributedString? { get set }
```

#### Discussion

When you translate an attributed string, the framework makes a best effort to preserve formatting and attributes such as accessibility instructions or timestamps for synchronized captions or lyrics.

The following example marks coordinates that VoiceOver spells out. When translated, VoiceOver spells out the translated coordinates character by character instead of reading them as full numbers:

```swift
import SwiftUI
import Translation

var attributedSource = AttributedString("The GPS coordinates are N37°47'11.5\" W122°25'34.2\"")

// Find the coordinate's range.
if let coordinatesRange = attributedSource.range(of: "N37°47'11.5\" W122°25'34.2\"") {
    // Mark coordinates for VoiceOver to spell out.
    attributedSource[coordinatesRange].accessibilitySpeechSpellsOutCharacters = true
}

// In your translation task translate the attributed text.
.translationTask(configuration) { session in
    do {

        let response = try await session.translate(attributedSource)

        // Preserve the spell out attribute for the Spanish translation.
        // VoiceOver reads: "Las coordenadas GPS son N - tres - siete -
        // grados, and so on."
        if var translated = response.attributedTargetText {
            // Set the language so VoiceOver uses the correct voice.
            translated.languageIdentifier = response.targetLanguage.languageCode?.identifier
        }
    } catch {
        // Handle any errors.
    }
}
```

When translating transcribed speech, the framework preserves time ranges so you can synchronize translated captions to the original audio. The Speech framework provides time ranges when you transcribe audio with [`SFSpeechRecognizer`](https://developer.apple.com/documentation/Speech/SFSpeechRecognizer). The following example shows setting time ranges and reads them back from the translation:

```swift
import SwiftUI
import Translation
import CoreMedia
import Speech
import AVFoundation

// Create a transcription with time ranges.
var transcription = AttributedString("Hello World")

// Set time ranges indicating when each word was spoken.
if let helloRange = transcription.range(of: "Hello") {
    transcription[helloRange][AttributeScopes.SpeechAttributes.TimeRangeAttribute.self] =
        CMTimeRange(start: CMTime(seconds: 0.0, preferredTimescale: 600),
                    duration: CMTime(seconds: 0.6, preferredTimescale: 600))
}

if let worldRange = transcription.range(of: "World") {
    transcription[worldRange][AttributeScopes.SpeechAttributes.TimeRangeAttribute.self] =
        CMTimeRange(start: CMTime(seconds: 0.6, preferredTimescale: 600),
                    duration: CMTime(seconds: 0.15, preferredTimescale: 600))
}

// In your translation task translate the transcription with the specified range in place.
.translationTask(configuration) { session in
    do {
        let response = try await session.translate(transcription)

        // Read preserved time ranges to synchronize captions to audio playback.
        if let translated = response.attributedTargetText {
            for run in translated.runs {
                if let timeRange = run[AttributeScopes.SpeechAttributes.TimeRangeAttribute.self] {
                    let start = CMTimeGetSeconds(timeRange.start)
                    let end = CMTimeGetSeconds(CMTimeRangeGetEnd(timeRange))
                    // Highlight the translated word when audio is between start and end.
                }
            }
        }
    } catch {
        // Handle any errors.
    }
}
```

## See Also

- [var sourceText: String](translationsession/request/sourcetext.md)
  The plain text input to translate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/request/attributedsourcetext)*