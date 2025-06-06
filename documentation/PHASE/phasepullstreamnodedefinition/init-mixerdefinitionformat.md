# init(mixerDefinition:format:)

**Framework**: PHASE  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
init(mixerDefinition: PHASEMixerDefinition, format: AVAudioFormat)
```

#### Discussion

```None
@method initWithMixerDefinition:format
@abstract Create a pull stream node definition
@param mixerDefinition
    The mixer definition this stream will be assigned to
@param format
    The AVAudioFormat object that will define the attributes of the audio this node will accept.
    Only Core Audio's standard deinterleaved 32-bit floating-point formats are supported.
@return
    A new PHASEPullStreamNodeDefinition object
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasepullstreamnodedefinition/init(mixerdefinition:format:))*