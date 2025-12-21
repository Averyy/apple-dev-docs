# isAvailable

**Framework**: GameKit  
**Kind**: property

A Boolean value that determines whether or not the session wants to connect to new peers.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isAvailable: Bool { get set }
```

#### Discussion

When [`isAvailable`](gksession/isavailable.md) is [`true`](https://developer.apple.com/documentation/Swift/true), the session is visible to other peers based on its [`sessionMode`](gksession/sessionmode.md) property. When [`isAvailable`](gksession/isavailable.md) is set to [`false`](https://developer.apple.com/documentation/Swift/false), it remains connected to peers, but is no longer visible to nonconnected peers. The default is [`false`](https://developer.apple.com/documentation/Swift/false).

Typically, your application configures the session object with a delegate and data receiver, and then sets [`isAvailable`](gksession/isavailable.md) to [`true`](https://developer.apple.com/documentation/Swift/true). When the delegate finishes connecting to peers, it should set the session’s [`isAvailable`](gksession/isavailable.md) property to [`false`](https://developer.apple.com/documentation/Swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/isavailable)*