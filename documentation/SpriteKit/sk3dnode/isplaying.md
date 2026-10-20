# isPlaying

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the scene is playing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isPlaying: Bool { get set }
```

```objc
@property (getter=isPlaying) BOOL playing;
```

#### Discussion

If the value of this property is [`false`](../../Swift/false.md) (the default), SceneKit does not increment the scene time, so animations associated with the scene do not play. Change this property’s value to [`true`](../../Swift/true.md) to start animating the scene.

## See Also

### Animating a 3D Node’s Content in Scene Kit
- [var loops: Bool](./loops.md)
  A Boolean value that determines whether Scene Kit restarts the scene time after all animations in the scene have played.
- [var sceneTime: TimeInterval](./scenetime.md)
  The current scene time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/isplaying)*