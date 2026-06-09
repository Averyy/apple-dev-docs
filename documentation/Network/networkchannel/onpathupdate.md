# onPathUpdate(_:)

**Framework**: Network  
**Kind**: method

Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
func onPathUpdate(_ handler: @escaping @isolated(any) @Sendable (Self, NWPath) -> Void) -> Self
```

#### Discussion

This closure will inherit the isolation domain of the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkchannel/onpathupdate(_:))*