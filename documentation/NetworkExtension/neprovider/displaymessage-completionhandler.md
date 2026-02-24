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
- `completionHandler`: A block that the system calls after you call this method. The details of the call can vary, as follows: - If the system can’t display the message, or if you call the `displayMessage:completionHandler:` method in an [`NEFilterDataProvider`](nefilterdataprovider.md) instance, then the system calls the `completionHandler` block immediately after you call the method, and sets the block’s `success` parameter value to [`false`](https://developer.apple.com/documentation/Swift/false).
- If the system successfully displays the message to the user, then the system calls the `completionHandler` block when the user dismisses the message, and sets the `success` parameter value to [`true`](https://developer.apple.com/documentation/Swift/true).


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neprovider/displaymessage(_:completionhandler:))*