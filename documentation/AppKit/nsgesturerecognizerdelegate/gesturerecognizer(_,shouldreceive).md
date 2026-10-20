# gestureRecognizer(_:shouldReceive:)

**Framework**: AppKit  
**Kind**: method

Called, for a new touch, before the system calls the `touchesBegan:withEvent:` method on the gesture recognizer. Return `NO` to prevent the gesture recognizer from seeing this touch.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer, shouldReceive touch: NSTouch) -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:))*