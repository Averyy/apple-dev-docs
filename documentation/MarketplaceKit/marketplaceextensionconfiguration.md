# MarketplaceExtensionConfiguration

**Framework**: MarketplaceKit  
**Kind**: protocol

The type for a marketplace extension’s configuration object.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
@preconcurrency protocol MarketplaceExtensionConfiguration : AppExtensionConfiguration
```

#### Overview

A marketplace extension ([`MarketplaceExtension`](marketplaceextension.md)) property [`configuration`](https://developer.apple.com/documentation/ExtensionFoundation/AppExtension/configuration-swift.property) adopts this protocol.

## Relationships

### Inherits From
- [AppExtensionConfiguration](../ExtensionFoundation/AppExtensionConfiguration.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MarketplaceExtension](marketplaceextension.md)
  An extension that facilitates authentication, installation, and launching a marketplace with deep links.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplaceextensionconfiguration)*