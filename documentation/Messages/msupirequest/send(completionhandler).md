# send(completionHandler:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func send(completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
func send() async -> Bool
```

```objc
- (void) sendWithCompletionHandler:(void (^)(BOOL sent)) completionHandler;
```

## Discussion

Sends this UPI request.

## Parameters

- `completionHandler`: A completion handler called when the message has been sent or has failed to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msupirequest/send(completionhandler:))*