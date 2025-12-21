# MarketplaceExtension

**Framework**: MarketplaceKit  
**Kind**: protocol

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
protocol MarketplaceExtension : AppExtension, Sendable
```

## Topics

### Instance Methods
- [func additionalHeaders(for: URLRequest, account: String) -> [String : String]?](marketplaceextension/additionalheaders(for:account:).md)
- [func automaticUpdates(for: [AppVersion]) async throws -> [AutomaticUpdate]](marketplaceextension/automaticupdates(for:).md)
- [func availableAppVersions(forAppleItemIDs: [AppleItemID]) -> [AppVersion]?](marketplaceextension/availableappversions(forappleitemids:).md)
- [func requestFailed(with: HTTPURLResponse) -> Bool](marketplaceextension/requestfailed(with:).md)

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MarketplaceExtensionConfiguration](marketplaceextensionconfiguration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/marketplaceextension)*