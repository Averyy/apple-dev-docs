# onViabilityUpdate(_:)

**Framework**: Network  
**Kind**: method

Set a closure to be called when the connection’s viability changes, which may be called multiple times until the connection is cancelled.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@discardableResult
func onViabilityUpdate(_ handler: @escaping @isolated(any) @Sendable (Self, Bool) -> Void) -> Self
```

#### Discussion

Connections that are not currently viable do not have a route, and packets will not be sent or received. There is a possibility that the connection will become viable again when network connectivity changes.

This closure will inherit the isolation domain of the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/onviabilityupdate(_:))*