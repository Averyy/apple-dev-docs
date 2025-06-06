# glkViewControllerUpdate(_:)

**Framework**: GLKit  
**Kind**: method  
**Required**: Yes

Called before each frame is displayed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
func glkViewControllerUpdate(_ controller: GLKViewController)
```

#### Discussion

This method is used by your application if it wants to updates state information on each frame of animation. A typical implementation might read the controller’s [`timeSinceLastUpdate`](glkviewcontroller/timesincelastupdate.md) property to determine how much time has actually passed, and use that time to calculate the positions for any objects to be rendered in the next frame.

## Parameters

- `controller`: The controller that is about to display a new frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate/glkviewcontrollerupdate(_:))*