# default

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The default appearance and layout for the Now Playing interface.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
class var `default`: CPNowPlayingMode { get }
```

```objc
@property (class, nonatomic, readonly) CPNowPlayingMode * defaultNowPlayingMode;
```

## Discussion

This mode shows the currently playing audio track, either on its own or as part of a playlist. With this layout, you specify artist, album, and track information for the current content. You can also add buttons for playlist-related behaviors such as shuffle and repeat modes.

If you change the mode of the Now Playing interface, return the interface to the default mode after the sporting event ends.

## See Also

### Creating a playing mode
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingmode/default)*