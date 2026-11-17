# playbackAction

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The action to perform on the media item when someone selects it.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var playbackAction: CPPlaybackConfiguration.Action { get }
```

```objc
@property (nonatomic, assign, readonly) CPPlaybackAction playbackAction;
```

## Discussion

When someone selects an item, this property tells the system whether to begin playing the item. You can direct the system to play or pause the item, play the item from the beginning, or do nothing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration/playbackaction)*