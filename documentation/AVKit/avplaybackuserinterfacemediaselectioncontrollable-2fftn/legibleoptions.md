# legibleOptions

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Array of available subtitle and caption track options. This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<AVPlaybackUserInterfaceMediaSelectionOption *> * legibleOptions;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacemediaselectioncontrollable-2fftn/legibleoptions)*