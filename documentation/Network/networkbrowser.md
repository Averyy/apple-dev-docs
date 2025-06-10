# NetworkBrowser

**Framework**: Network  
**Kind**: class

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
final class NetworkBrowser<Provider> where Provider : BrowserProvider
```

## Topics

### Initializers
- [convenience init(for: Provider, using: NWParameters?)](networkbrowser/init(for:using:).md)
- [init(provider: Provider, using: NWParameters?)](networkbrowser/init(provider:using:).md)
### Instance Methods
- [func onStateUpdate(NetworkBrowser<Provider>.StateUpdateHandler?) -> Self](networkbrowser/onstateupdate(_:).md)
- [func run<Return>(([Provider.Endpoint]) async throws -> NetworkBrowser<Provider>.Result<Return>) async throws -> Return](networkbrowser/run(_:)-1zk2m.md)
- [func run(([Provider.Endpoint]) async throws -> Void) async throws](networkbrowser/run(_:)-31x4b.md)
### Type Aliases
- [NetworkBrowser.State](networkbrowser/state.md)
- [NetworkBrowser.StateUpdateHandler](networkbrowser/stateupdatehandler.md)
### Enumerations
- [NetworkBrowser.Result](networkbrowser/result.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkbrowser)*