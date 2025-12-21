# onPathUpdate(_:)

**Framework**: Network  
**Kind**: method

Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled.

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
@discardableResult
final func onPathUpdate(_ handler: @escaping @isolated(any) (NetworkConnection<ApplicationProtocol>, NWPath) -> Void) -> Self
```

#### Discussion

This closure will inherit the isolation domain of the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/onpathupdate(_:))*