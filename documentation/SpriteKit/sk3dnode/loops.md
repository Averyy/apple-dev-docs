# loops

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether Scene Kit restarts the scene time after all animations in the scene have played.

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
var loops: Bool { get set }
```

```objc
@property (nonatomic) BOOL loops;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md) (the default), SceneKit returns the scene time to zero after all animations associated with the scene have played, causing those animations to repeat. Otherwise, SceneKit stops playing the scene when all animations have completed.

## See Also

### Animating a 3D Node’s Content in Scene Kit
- [var isPlaying: Bool](./isplaying.md)
  A Boolean value that determines whether the scene is playing.
- [var sceneTime: TimeInterval](./scenetime.md)
  The current scene time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sk3dnode/loops)*