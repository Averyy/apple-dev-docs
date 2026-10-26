# audioOptions

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Array of available audio track options. This includes all audio streams provided by the media source such as different languages, director’s commentary, and alternative audio mixes. Options are ordered by preference with the primary language or default audio track typically appearing first. May be empty for content without selectable audio options. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<AVPlaybackUserInterfaceMediaSelectionOption *> * audioOptions;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn/audiooptions)*