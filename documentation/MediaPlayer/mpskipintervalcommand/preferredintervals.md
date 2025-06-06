# preferredIntervals

**Framework**: Media Player  
**Kind**: property

The available skip intervals, in seconds, for a media item.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var preferredIntervals: [NSNumber] { get set }
```

#### Discussion

The `preferredIntervals` property holds an array of [`TimeInterval`](https://developer.apple.com/documentation/Foundation/TimeInterval) objects that designate different skip intervals for a media item. The skip intervals are defined in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand/preferredintervals)*