# audioOptions

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Array of available audio track options for selection. This includes all audio streams provided by the media source such as different languages, audio descriptions, director’s commentary, and alternative audio mixes. Options are ordered by preference with the primary language or default audio track typically appearing first. May be empty for content without selectable audio options. Must be key-value observable.

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<AVInterfaceMediaSelectionOptionSource *> * audioOptions;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectioncontrollable/audiooptions)*