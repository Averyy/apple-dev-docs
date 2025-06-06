# sendPing(pongReceiveHandler:)

**Framework**: Foundation  
**Kind**: method

Sends a ping frame from the client side, with a closure to receive the pong from the server endpoint.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func sendPing(pongReceiveHandler: @escaping ((any Error)?) -> Void)
```

#### Discussion

When sending multiple pings, the task always calls `pongReceiveHandler` in the order it sent the pings.

## Parameters

- `pongReceiveHandler`: A closure called by the task when it receives the pong from the server. The block/closure receives an   that indicates a lost connection or other problem, or   if no error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/sendping(pongreceivehandler:))*