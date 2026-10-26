# supportedSeekCapabilities

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

An option set indicating which timeline navigation operations are supported by this media source. This property defines the available navigation capabilities, including precise seeking to specific time positions and accelerated scanning for fast-forward/rewind operations. The supported modes may vary based on content type, licensing restrictions, or technical limitations of the underlying media format. Must be key-value observable.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (nonatomic, readonly) AVPlaybackUserInterfaceSeekCapabilities supportedSeekCapabilities;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/supportedseekcapabilities)*