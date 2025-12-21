# requestLicenseRenewal(appleItemIDs:)

**Framework**: MarketplaceKit  
**Kind**: method

Instructs iOS to request an updated app license from your marketplace server for the given app identifier.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
nonisolated
final func requestLicenseRenewal(appleItemIDs: [UInt64]) async throws
```

## See Also

- [func requestAppUpdate(AppLibrary.InstallationRequest) async throws](applibrary/requestappupdate(_:).md)
  Requests an app update for the given app distribution package and account information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/requestlicenserenewal(appleitemids:))*