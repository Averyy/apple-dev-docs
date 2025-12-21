# NetworkBrowser

**Framework**: Network  
**Kind**: class

Discover advertised services and devices on the network.

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
final class NetworkBrowser<Provider> where Provider : BrowserProvider
```

#### Overview

Whenever services become available, get modified, or go away, the browser will generate a set of browse results tracking those changes. You can subscribe to and receive these updates as long as the browser is active.

## Topics

### Initializers
- [init(for: Provider, using: NWParameters?)](networkbrowser/init(for:using:).md)
  Create a browser that will browse for the service specified by a BrowserProvider, with parameters.
### Instance Methods
- [func onStateUpdate((NetworkBrowser<Provider>, NetworkBrowser<Provider>.State) -> Void) -> Self](networkbrowser/onstateupdate(_:).md)
  Set a closure to be called when the browser’s state changes.
- [func run(([Provider.Endpoint]) async throws -> Void) async throws](networkbrowser/run(_:)-31x4b.md)
  Run the browser and receive updates when when the set of discovered endpoints change.
- [func run<Return>(([Provider.Endpoint]) async throws -> NetworkBrowser<Provider>.RunResult<Return>) async throws -> Return](networkbrowser/run(_:)-wqyo.md)
### Type Aliases
- [NetworkBrowser.StateUpdateHandler](networkbrowser/stateupdatehandler.md)
### Enumerations
- [NetworkBrowser.RunResult](networkbrowser/runresult.md)
- [NetworkBrowser.State](networkbrowser/state.md)
  Possible states for the browser to be in.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkbrowser)*