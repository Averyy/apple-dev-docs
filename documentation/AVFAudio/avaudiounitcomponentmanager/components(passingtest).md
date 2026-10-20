# components(passingTest:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSArray<AVAudioUnitComponent *> *) componentsPassingTest:(BOOL (^)(AVAudioUnitComponent *comp, BOOL *stop)) testHandler;
```

#### Return Value

An array of audio components that pass the test.

#### Discussion

For each audio component the manager finds, the system calls the block method. If the block returns [`true`](../../Swift/true.md), the method adds `AVAudioComponent` instance to the array.

## Parameters

- `testHandler`: The block to apply to the audio unit components.

  The block takes two parameters.

  - **comp**: A block to test.
  - **stop**: A reference to a Boolean value. To stop further processing of the search, the block sets the value to [`true`](../../Swift/true.md). The stop argument is an out-only argument. Only set this Boolean to [`true`](../../Swift/true.md) within the block.

  The block returns a Boolean value that indicates whether `comp` passes the test. Returning [`true`](../../Swift/true.md) stops further processing of the audio components.

## See Also

### Getting matching audio components
- [func components(matching: AudioComponentDescription) -> [AVAudioUnitComponent]](./components%28matching%29-9qt94.md)
  Gets an array of audio component objects that match the description.
- [func components(matching: NSPredicate) -> [AVAudioUnitComponent]](./components%28matching%29-96l2c.md)
  Gets an array of audio component objects that match the search predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponentmanager/components(passingtest:))*