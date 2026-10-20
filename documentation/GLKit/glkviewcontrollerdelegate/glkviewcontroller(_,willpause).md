# glkViewController(_:willPause:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Instance Method

Called before the rendering loop is paused or resumed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
optional func glkViewController(_ controller: GLKViewController, willPause pause: Bool)
```

```objc
- (void) glkViewController:(GLKViewController *) controller willPause:(BOOL) pause;
```

## Parameters

- `controller`: The controller that is about to change the rendering loop state.
- `pause`: [`true`](../../Swift/true.md) if the loop is being paused, [`false`](../../Swift/false.md) if it is being resumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate/glkviewcontroller(_:willpause:))*