# displayMessage(_:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Call this method from your [`NEProvider`](neprovider.md) subclass if you want to display a message to the person using the app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
func displayMessage(_ message: String) async -> Bool
```

## Parameters

- `message`: The message you want to display to the person using the app.
- `completionHandler`: A block that the system calls after you call this method. The details of the call can vary, as follows:


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/displaymessage(_:completionhandler:))*