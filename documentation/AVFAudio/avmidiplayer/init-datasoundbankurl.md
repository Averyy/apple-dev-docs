# init(data:soundBankURL:)

**Framework**: AVFAudio  
**Kind**: init

Creates a player to play MIDI data with the specified soundbank.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(data: Data, soundBankURL bankURL: URL?) throws
```

#### Return Value

A new MIDI player, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if an error occurred.

## Parameters

- `data`: The data to play.
- `bankURL`: The URL of the sound bank. The sound bank must be a SoundFont2 or DLS bank. In macOS, you can pass   for the bank URL argument to use the default sound bank. In iOS, you must always pass a valid bank file.

## See Also

- [init(contentsOf: URL, soundBankURL: URL?) throws](avmidiplayer/init(contentsof:soundbankurl:).md)
  Creates a player to play a MIDI file with the specified soundbank.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/init(data:soundbankurl:))*