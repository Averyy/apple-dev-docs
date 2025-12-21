# components(passingTest:)

**Framework**: AVFAudio  
**Kind**: method

Gets an array of audio components that pass the block method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func components(passingTest testHandler: @escaping (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]
```

#### Return Value

An array of audio components that pass the test.

#### Discussion

For each audio component the manager finds, the system calls the block method. If the block returns [`true`](https://developer.apple.com/documentation/Swift/true), the method adds `AVAudioComponent` instance to the array.

## Parameters

- `testHandler`: The block returns a Boolean value that indicates whether   passes the test. Returning   stops further processing of the audio components.

## See Also

- [func components(matching: AudioComponentDescription) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(matching:)-9qt94.md)
  Gets an array of audio component objects that match the description.
- [func components(matching: NSPredicate) -> [AVAudioUnitComponent]](avaudiounitcomponentmanager/components(matching:)-96l2c.md)
  Gets an array of audio component objects that match the search predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager/components(passingtest:))*