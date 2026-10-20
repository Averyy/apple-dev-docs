# requestAppUpdate(_:)

**Framework**: MarketplaceKit  
**Kind**: method  
**Role**: Instance Method

Requests an app update for the given app distribution package and account information.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
nonisolated
final func requestAppUpdate(_ request: AppLibrary.InstallationRequest) async throws
```

## See Also

### Updating apps
- [func requestLicenseRenewal(appleItemIDs: [UInt64]) async throws](./requestlicenserenewal%28appleitemids%29.md)
  Instructs the system to request an updated app license from your marketplace server for the given app identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/requestappupdate(_:))*