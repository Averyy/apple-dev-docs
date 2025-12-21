# NWBrowser

**Framework**: Network  
**Kind**: class

An object you use to browse for available network services.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
final class NWBrowser
```

## Topics

### Essentials
- [NSBonjourServices](../BundleResources/Information-Property-List/NSBonjourServices.md)
  Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../BundleResources/Information-Property-List/NSLocalNetworkUsageDescription.md)
  A message that tells people why the app is requesting access to the local network.
### Browsing for Services
- [init(for: NWBrowser.Descriptor, using: NWParameters)](nwbrowser/init(for:using:).md)
  Initializes a browser with a type of service to discover.
- [NWBrowser.Descriptor](nwbrowser/descriptor-swift.enum.md)
  A service description used to discover Bonjour services.
- [func start(queue: DispatchQueue)](nwbrowser/start(queue:).md)
  Starts browsing for services, and sets the queue on which all browser events will be delivered.
- [var browseResultsChangedHandler: ((Set<NWBrowser.Result>, Set<NWBrowser.Result.Change>) -> Void)?](nwbrowser/browseresultschangedhandler.md)
  A handler that delivers updates about discovered services.
- [NWBrowser.Result](nwbrowser/result.md)
  A set of discovered services and changes from the last result.
- [var browseResults: Set<NWBrowser.Result>](nwbrowser/browseresults.md)
  The list of discovered services.
### Managing Browsers
- [var stateUpdateHandler: ((NWBrowser.State) -> Void)?](nwbrowser/stateupdatehandler.md)
  A handler that receives browser state updates.
- [NWBrowser.State](nwbrowser/state-swift.enum.md)
  States indicating whether a browser is able to discover services.
- [var state: NWBrowser.State](nwbrowser/state-swift.property.md)
  The current state of the browser.
- [func cancel()](nwbrowser/cancel.md)
  Stops browsing for services.
### Inspecting Browsers
- [let descriptor: NWBrowser.Descriptor](nwbrowser/descriptor-swift.property.md)
  The service descriptor with which the browser was initialized.
- [let parameters: NWParameters](nwbrowser/parameters.md)
  The parameters with which the browser was initialized.
- [var queue: DispatchQueue?](nwbrowser/queue.md)
  The queue on which browser events are delivered.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NWConnection](nwconnection.md)
  A bidirectional data connection between a local endpoint and a remote endpoint.
- [class NWListener](nwlistener.md)
  An object you use to listen for incoming network connections.
- [class NWConnectionGroup](nwconnectiongroup.md)
  An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [class NWEthernetChannel](nwethernetchannel.md)
  An object you use to send and receive custom Ethernet frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser)*