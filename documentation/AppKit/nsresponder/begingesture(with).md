# beginGesture(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the user has begun a touch gesture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func beginGesture(with event: NSEvent)
```

#### Discussion

The event will be sent to the view under the touch in the key window.

Note that this method is no longer called on apps that link against macOS 10.11 and later. If you need to access the phases of a specific gesture, you can implement the responder for that gesture and examine its [`phase`](nsevent/phase-swift.property.md) property instead.

## Parameters

- `event`: An event object representing the gesture beginning.

## See Also

- [func endGesture(with: NSEvent)](nsresponder/endgesture(with:).md)
  Informs the receiver that the user has ended a touch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/begingesture(with:))*