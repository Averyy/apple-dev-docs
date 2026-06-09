# NetworkActorInterruptionHandler

**Framework**: Network  
**Kind**: typealias

A handler that is invoked when the underlying connection is interrupted. An attempt at creating a new connection will occur if another remote call is invoked on the same remote instance of an actor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias NetworkActorInterruptionHandler = ((any Error)?) -> Void
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkactorinterruptionhandler)*