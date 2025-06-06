# components(matching:)

**Framework**: AVFAudio  
**Kind**: method

Gets an array of audio component objects that match the description.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func components(matching desc: AudioComponentDescription) -> [AVAudioUnitComponent]
```

#### Return Value

An array of `AVAudioComponent` objects that match the `description`.

#### Discussion

- desc: The [`AudioComponentDescription`](https://developer.apple.com/documentation/AudioToolbox/AudioComponentDescription) structure to match. The method uses the `type`, `subtype` and `manufacturer` fields to search for matching audio units. A value of `0` for any of these fields is a wildcard and returns the first match the method finds.

## See Also

- [func components(matching: NSPredicate) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(matching:)-96l2c.md)
  Gets an array of audio component objects that match the search predicate.
- [func components(passingTest: (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(passingtest:).md)
  Gets an array of audio components that pass the block method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager/components(matching:)-9qt94)*