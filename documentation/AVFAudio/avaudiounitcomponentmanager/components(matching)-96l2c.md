# components(matching:)

**Framework**: AVFAudio  
**Kind**: method

Gets an array of audio component objects that match the search predicate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func components(matching predicate: NSPredicate) -> [AVAudioUnitComponent]
```

#### Return Value

An array of `AVAudioComponent` objects that match the predicate.

#### Discussion

You use the audio component’s information or tags to build search criteria, such as `“typeName CONTAINS 'Effect'"` or `“tags IN {'Sampler', 'MIDI'}"`.

## Parameters

- `predicate`: The search predicate.

## See Also

- [func components(matching: AudioComponentDescription) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(matching:)-9qt94.md)
  Gets an array of audio component objects that match the description.
- [func components(passingTest: (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(passingtest:).md)
  Gets an array of audio components that pass the block method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager/components(matching:)-96l2c)*