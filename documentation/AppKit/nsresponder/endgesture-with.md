# endGesture(with:)

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the user has ended a touch gesture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func endGesture(with event: NSEvent)
```

#### Discussion

Note that this method is no longer called on apps that link against macOS 10.11 and later. If you need to access the phases of a specific gesture, you can implement the responder for that gesture and examine its [`phase`](nsevent/phase-swift.property.md) property instead.

## Parameters

- `event`: An event object representing the gesture end.

## See Also

- [func beginGesture(with: NSEvent)](nsresponder/begingesture(with:).md)
  Informs the receiver that the user has begun a touch gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/endgesture(with:))*