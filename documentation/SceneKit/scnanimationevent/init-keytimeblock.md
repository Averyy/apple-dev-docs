# init(keyTime:block:)

**Framework**: SceneKit  
**Kind**: init

Creates an animation event.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
convenience init(keyTime time: CGFloat, block eventBlock: @escaping SCNAnimationEventBlock)
```

#### Return Value

An animation event object.

#### Discussion

The `time` parameter is relative to the duration of the animation the event is attached to. For example, an event with a time of `0.5` triggers when the animation is halfway complete, and an event with a time of `1.0` triggers when the animation ends.

## Parameters

- `time`: A number between   and   specifying the relative time for triggering the event.
- `eventBlock`: A block to call at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimationevent/init(keytime:block:))*