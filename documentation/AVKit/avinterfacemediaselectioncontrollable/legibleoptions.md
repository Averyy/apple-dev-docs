# legibleOptions

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

Array of available subtitle and caption track options for selection. This includes text overlays in different languages, closed captions for accessibility, forced narrative subtitles, and sign language interpretation tracks. May be empty for content without text tracks. Must be key-value observable.

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<AVInterfaceMediaSelectionOptionSource *> * legibleOptions;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinterfacemediaselectioncontrollable/legibleoptions)*