# init(contentsOf:soundBankURL:)

**Framework**: AVFAudio  
**Kind**: init

Creates a player to play a MIDI file with the specified soundbank.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(contentsOf inURL: URL, soundBankURL bankURL: URL?) throws
```

#### Return Value

A new MIDI player, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if an error occurred.

## Parameters

- `inURL`: The URL of the file to play.
- `bankURL`: The URL of the sound bank. The sound bank must be in SoundFont2 or DLS format. In macOS, you can pass   for the bank URL argument to use the default sound bank. In iOS, you must always pass a valid bank file.

## See Also

- [init(data: Data, soundBankURL: URL?) throws](avmidiplayer/init(data:soundbankurl:).md)
  Creates a player to play MIDI data with the specified soundbank.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/init(contentsof:soundbankurl:))*