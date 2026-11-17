# playbackConfiguration

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The media-related metadata to associate with the item.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@NSCopying
var playbackConfiguration: CPPlaybackConfiguration? { get set }
```

```objc
@property (nonatomic, copy, nullable) CPPlaybackConfiguration * playbackConfiguration;
```

## Discussion

Assign a value to this property to associate media-related metadata with an item. The default value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplayableitem/playbackconfiguration)*