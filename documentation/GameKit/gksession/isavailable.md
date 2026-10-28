# isAvailable

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether or not the session wants to connect to new peers.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
var isAvailable: Bool { get set }
```

```objc
@property (getter=isAvailable) BOOL available;
```

## Discussion

When [`isAvailable`](./isavailable.md) is [`true`](../../Swift/true.md), the session is visible to other peers based on its [`sessionMode`](./sessionmode.md) property. When [`isAvailable`](./isavailable.md) is set to [`false`](../../Swift/false.md), it remains connected to peers, but is no longer visible to nonconnected peers. The default is [`false`](../../Swift/false.md).

Typically, your application configures the session object with a delegate and data receiver, and then sets [`isAvailable`](./isavailable.md) to [`true`](../../Swift/true.md). When the delegate finishes connecting to peers, it should set the session’s [`isAvailable`](./isavailable.md) property to [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/isavailable)*