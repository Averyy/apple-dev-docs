# newConnectionLimit

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

Configure the listener’s new connection limit.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
final var newConnectionLimit: Int { get set }
```

## Discussion

Use the value NWListener.InfiniteConnectionLimit to disable connection limits.

If the value is not NWListener.InfiniteConnectionLimit, the value will be decremented by 1 every time a new connection is received. When the value reaches 0, the new connection handler will no longer be invoked until the the limit is increased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networklistener/newconnectionlimit)*