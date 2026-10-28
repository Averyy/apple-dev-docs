# animationEvents

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

For animations attached to SceneKit objects, a list of events attached to an animation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS

## Declaration

```swift
var animationEvents: [SCNAnimationEvent]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<SCNAnimationEvent *> * animationEvents;
```

## Discussion

An array of [`SCNAnimationEvent`](../../SceneKit/scnanimationevent.md) objects, each of which adds a timed action to the animation.

For example, you can create animation events that play sound effects timed to match the footsteps of an animated game character or that add new nodes to the scene when an animation completes.

To attach animations to SceneKit objects, see [`SCNAnimatable`](../../SceneKit/scnanimatable.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimation/animationevents)*