# onStateUpdate(_:)

**Framework**: Network  
**Kind**: method

Set a closure to be called when the browser’s state changes.

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
final func onStateUpdate(_ handler: @escaping @isolated(any) @Sendable (NetworkBrowser<Provider>, NetworkBrowser<Provider>.State) -> Void) -> Self
```

#### Discussion

The closure may be called multiple times until the browser is cancelled.

The closure inherits the isolation domain of the caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkbrowser/onstateupdate(_:))*