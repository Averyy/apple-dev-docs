# onStateUpdate(_:)

**Framework**: Network  
**Kind**: method

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
final func onStateUpdate(_ handler: (@isolated(any) (NetworkConnection<ApplicationProtocol>, NWConnection.State) -> Void)?) -> Self
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkconnection/onstateupdate(_:)-2xbqu)*