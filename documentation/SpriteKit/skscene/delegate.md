# delegate

**Framework**: SpriteKit  
**Kind**: property

A delegate to be called during the animation loop.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var delegate: (any SKSceneDelegate)? { get set }
```

#### Discussion

When a delegate is present, when any of the animation loop methods steps are executed, your delegate is called. Typically, you use a delegate when you do not want to implement a scene subclass or if you want to dynamically change the scene behavior at runtime.

## See Also

- [Subclassing Scenes Versus Assigning a Delegate](subclassing-scenes-versus-assigning-a-delegate.md)
  Use a scene delegate to share app logic across various scenes.
- [protocol SKSceneDelegate](skscenedelegate.md)
  Methods that, when implemented, allow any class to participate in the SpriteKit render loop callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skscene/delegate)*