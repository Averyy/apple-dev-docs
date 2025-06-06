# glkViewController(_:willPause:)

**Framework**: GLKit  
**Kind**: method

Called before the rendering loop is paused or resumed.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- tvOS 9.0+

## Declaration

```swift
optional func glkViewController(_ controller: GLKViewController, willPause pause: Bool)
```

## Parameters

- `controller`: The controller that is about to change the rendering loop state.
- `pause`:   if the loop is being paused,   if it is being resumed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkviewcontrollerdelegate/glkviewcontroller(_:willpause:))*