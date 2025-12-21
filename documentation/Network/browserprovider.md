# BrowserProvider

**Framework**: Network  
**Kind**: protocol

BrowserProviders can be used when creating NetworkBrowsers.

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
protocol BrowserProvider : Sendable
```

## Topics

### Associated Types
- [associatedtype Endpoint : Connectable](browserprovider/endpoint.md)
### Type Methods
- [static func bonjour(String, domain: String?, includeTxtRecord: Bool) -> Bonjour](browserprovider/bonjour(_:domain:includetxtrecord:).md)
  Create a Bonjour browser provider used to browse for Bonjour services.
- [static func wifiAware(WASubscriberBrowser.Action, active: Duration?) -> Self](browserprovider/wifiaware(_:active:).md)
  Setup a `NetworkBrowser` to subscribe to Wi-Fi Aware services on selected, paired devices.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [Bonjour](bonjour.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/browserprovider)*