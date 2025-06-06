# instantiate(with:options:completionHandler:)

**Framework**: AVFAudio  
**Kind**: method

Creates an instance of an audio unit component asynchronously and wraps it in an audio unit class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func instantiate(with audioComponentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions = []) async throws -> AVAudioUnit
```

#### Discussion

You must create components with flags that include [`requiresAsyncInstantiation`](https://developer.apple.com/documentation/AudioToolbox/AudioComponentFlags/requiresAsyncInstantiation) asynchronously through this method if they’re for use with [`AVAudioEngine`](avaudioengine.md).

The [`AVAudioUnit`](avaudiounit.md) instance is usually a subclass that the method selects according to the components type. For example, [`AVAudioUnitEffect`](avaudiouniteffect.md), [`AVAudioUnitGenerator`](avaudiounitgenerator.md), [`AVAudioUnitMIDIInstrument`](avaudiounitmidiinstrument.md), or [`AVAudioUnitTimeEffect`](avaudiounittimeeffect.md).

## Parameters

- `audioComponentDescription`: The component to create.
- `options`: The options the method uses to create the component.
- `completionHandler`: A handler the framework calls in an arbitrary thread context when creation completes. Retain the   this handler provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounit/instantiate(with:options:completionhandler:))*