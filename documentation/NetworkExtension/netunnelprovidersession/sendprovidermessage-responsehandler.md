# sendProviderMessage(_:responseHandler:)

**Framework**: Network Extension  
**Kind**: method

Send a message to the Tunnel Provider extension. If the extension is not running, it should be launched to handle the message. If this method can’t start sending the message it reports an error in the `returnError` parameter. If an error occurs while sending the message or returning the result, `nil` should be sent to the response handler as notification.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func sendProviderMessage(_ messageData: Data, responseHandler: ((Data?) -> Void)? = nil) throws
```

#### Discussion

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `messageData`: An   object containing the message to be sent.
- `responseHandler`: An optional block that handles the response from the Tunnel Provider extension. Pass nil if no response is expected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/sendprovidermessage(_:responsehandler:))*