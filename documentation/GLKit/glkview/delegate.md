# delegate

**Framework**: GLKit  
**Kind**: property

The view’s delegate.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
@IBOutlet
@MainActor unowned(unsafe) var delegate: (any GLKViewDelegate)? { get set }
```

#### Discussion

A delegate is optional. If a delegate is provided, it is called instead of calling a [`draw(_:)`](https://developer.apple.com/documentation/UIKit/UIView/draw(_:)) method whenever the view’s contents need to be drawn. You should either subclass the view to override the `draw` method, or provide a delegate, but not both.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkview/delegate)*