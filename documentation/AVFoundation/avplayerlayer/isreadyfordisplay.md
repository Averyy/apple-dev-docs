# isReadyForDisplay

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the first video frame of the player’s current item is ready for display.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isReadyForDisplay: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isReadyForDisplay) BOOL readyForDisplay;
```

#### Discussion

Use this property to determine when to show or animate a player layer into view. You can display a player layer while this property value is [`false`](../../Swift/false.md), but the layer doesn’t present any content until the value becomes [`true`](../../Swift/true.md).

This property remains [`false`](../../Swift/false.md) for a player when its [`currentItem`](../avplayer/currentitem.md) contains no enabled video tracks.

This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlayer/isreadyfordisplay)*