# BrowserProvider

**Framework**: Network  
**Kind**: protocol

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
protocol BrowserProvider : Sendable
```

## Topics

### Associated Types
- [associatedtype Endpoint : Connectable](browserprovider/endpoint.md)
### Type Methods
- [static func bonjour(String, domain: String?, metadata: Bool) -> Bonjour](browserprovider/bonjour(_:domain:metadata:).md)
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