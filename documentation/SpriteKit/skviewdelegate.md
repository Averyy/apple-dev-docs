# SKViewDelegate

**Framework**: SpriteKit  
**Kind**: protocol

Methods to take custom control over the view’s render rate.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol SKViewDelegate : NSObjectProtocol
```

## Mentions

- [Getting Started with Nodes](getting-started-with-nodes.md)

#### Overview

By setting a SpriteKit view’s `delegate` with an object that implements [`SKViewDelegate`](skviewdelegate.md), you can precisely control the frame rate of a game or app. You may choose to do this to maintain a consistent frame rate for computationally intensive code or for special effects such as simulating cine film.

The following Swift code shows an example of a class that implements the SpriteKit view delegate protocol to reduce the frame rate to a specified value. With each call of [`view(_:shouldRenderAtTime:)`](skviewdelegate/view(_:shouldrenderattime:).md), it checks the time since the last render and if that value exceeds the required frame duration (`1 / fps`), the method returns [`true`](https://developer.apple.com/documentation/swift/true) and the frame is rendered.

```swift
class ViewDelegate: NSObject, SKViewDelegate {
    var lastRenderTime: TimeInterval = 0
    
    let fps: TimeInterval = 3
    
    public func view(_ view: SKView, shouldRenderAtTime time: TimeInterval) -> Bool {

        if time - lastRenderTime >= 1 / fps {
            lastRenderTime = time
            return true
        }
        else {
            return false
        }
        
    }
}
```

The return value of [`view(_:shouldRenderAtTime:)`](skviewdelegate/view(_:shouldrenderattime:).md) doesn’t change the speed of physics simulations and actions in a SpriteKit scene. However, if you return [`false`](https://developer.apple.com/documentation/swift/false), SpriteKit will skip updates and [`SKSceneDelegate`](skscenedelegate.md) methods are not called.

## Topics

### Instance Methods
- [func view(SKView, shouldRenderAtTime: TimeInterval) -> Bool](skviewdelegate/view(_:shouldrenderattime:).md)
  Specifies whether the view should render at the given time.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var isPaused: Bool](skview/ispaused.md)
  A Boolean value that indicates whether the view’s scene animations are paused.
- [var preferredFramesPerSecond: Int](skview/preferredframespersecond.md)
  The animation frame rate that the view uses to render its scene.
- [var delegate: (any SKViewDelegate)?](skview/delegate.md)
  A delegate that allows dynamic control of the view’s render rate.
- [var frameInterval: Int](skview/frameinterval.md)
  The number of frames that must pass before the scene is called to update its contents.
- [var preferredFrameRate: Float](skview/preferredframerate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skviewdelegate)*