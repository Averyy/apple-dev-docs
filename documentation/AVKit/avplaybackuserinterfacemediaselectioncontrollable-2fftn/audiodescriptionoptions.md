# audioDescriptionOptions

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Array of available audio description track options. Audio description tracks provide narrated descriptions of visual content for visually impaired viewers. Audio description options are distinct from those in `audioOptions` — they provide a narration layer played alongside the primary audio rather than replacing it. Options are ordered by preference with the primary language or default audio description track typically appearing first. May be empty for content without audio description tracks. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<AVPlaybackUserInterfaceMediaSelectionOption *> * audioDescriptionOptions;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiodescriptionoptions)*