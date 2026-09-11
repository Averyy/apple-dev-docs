# onPathUpdate(_:)

**Framework**: Network  
**Kind**: method

Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled.

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
func onPathUpdate(_ handler: @escaping @isolated(any) @Sendable (Self, NWPath) -> Void) -> Self
```

#### Discussion

This closure will inherit the isolation domain of the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/onpathupdate(_:))*