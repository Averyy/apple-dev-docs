# MarketplaceExtension

**Framework**: MarketplaceKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 17.4+ - Deprecated in 26.0
- iPadOS 17.4+ - Deprecated in 26.0

> **Deprecated**: Use MarketplaceAppExtension instead.

## Declaration

```swift
protocol MarketplaceExtension : AppExtension, Sendable
```

## Topics

### Instance Methods
- [func additionalHeaders(for: URLRequest, account: String) -> [String : String]?](./marketplaceextension/additionalheaders%28for,account%29.md)
- [func automaticUpdates(for: [AppVersion]) async throws -> [AutomaticUpdate]](./marketplaceextension/automaticupdates%28for%29.md)
- [func availableAppVersions(forAppleItemIDs: [AppleItemID]) -> [AppVersion]?](./marketplaceextension/availableappversions%28forappleitemids%29.md)
- [func requestFailed(with: HTTPURLResponse) -> Bool](./marketplaceextension/requestfailed%28with%29.md)

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/appextension.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Deprecations
- [protocol MarketplaceExtensionConfiguration](./marketplaceextensionconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplaceextension)*