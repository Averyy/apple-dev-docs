# delegate

**Framework**: ARKit  
**Kind**: property

An object you provide to receive captured video images and tracking information, or to respond to changes in session status.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
weak var delegate: (any ARSessionDelegate)? { get set }
```

#### Discussion

If you use the [`ARSCNView`](arscnview.md) or [`ARSKView`](arskview.md) class to display your AR experience, a session delegate isn’t necessary. Those views automatically display captured video images and coordinate SceneKit or SpriteKit content to track device and camera motion.

If you create your own visualization for an AR experience using Metal or other rendering technologies, set a session delegate. Your delegate object periodically receives [`ARFrame`](arframe.md) objects captured by the session. These objects contain video frame images for you to display and AR scene information you can use to coordinate display of the scene elements you render.

## See Also

- [var delegateQueue: dispatch_queue_t?](arsession/delegatequeue.md)
  The dispatch queue through which the session calls your delegate methods.
- [protocol ARSessionDelegate](arsessiondelegate.md)
  Methods you can implement to receive captured video frame images and tracking state from an AR session.
- [protocol ARSessionObserver](arsessionobserver.md)
  Methods you can implement to respond to changes in the state of an AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/delegate)*