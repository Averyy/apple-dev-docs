# init(data:soundBankURL:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithData:(NSData *) data soundBankURL:(NSURL *) bankURL error:(NSError **) outError;
```

## Return Value

A new MIDI player, or [`nil`](../../ObjectiveC/nil-227m0.md) if an error occurred.

## Parameters

- `data`: The data to play.
- `bankURL`: The URL of the sound bank. The sound bank must be a SoundFont2 or DLS bank. In macOS, you can pass [`nil`](../../ObjectiveC/nil-227m0.md) for the bank URL argument to use the default sound bank. In iOS, you must always pass a valid bank file.

## See Also

### Creating a MIDI player
- [init(contentsOf: URL, soundBankURL: URL?) throws](./init%28contentsof,soundbankurl%29.md)
  Creates a player to play a MIDI file with the specified soundbank.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avmidiplayer/init(data:soundbankurl:))*