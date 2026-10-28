# components(matching:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<AVAudioUnitComponent *> *) componentsMatchingPredicate:(NSPredicate *) predicate;
```

## Return Value

An array of `AVAudioComponent` objects that match the predicate.

## Discussion

You use the audio component’s information or tags to build search criteria, such as `“typeName CONTAINS 'Effect'"` or `“tags IN {'Sampler', 'MIDI'}"`.

## Parameters

- `predicate`: The search predicate.

## See Also

### Getting matching audio components
- [func components(matching: AudioComponentDescription) -> [AVAudioUnitComponent]](./components%28matching%29-9qt94.md)
  Gets an array of audio component objects that match the description.
- [func components(passingTest: (AVAudioUnitComponent, UnsafeMutablePointer<ObjCBool>) -> Bool) -> [AVAudioUnitComponent]](./components%28passingtest%29.md)
  Gets an array of audio components that pass the block method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager/components(matching:)-96l2c)*