# alternativeDistributionPackage

**Framework**: MarketplaceKit  
**Kind**: property

A URL to the app’s assembled alternative distribution package.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let alternativeDistributionPackage: URL
```

#### Discussion

You ingest an available app’s alternative distribution package from App Store Connect in advance, then set this URL to the location that you store the alternative distribution package on your server.

For more information, see [`Ingesting an alternative distribution package`](ingesting-an-alternative-distribution-package.md).

## See Also

- [let appleItemID: AppleItemID](installmetadata/appleitemid.md)
  A unique identifier for the app to install.
- [var appShareURL: URL?](installmetadata/appshareurl.md)
  A URL to a product landing page for the app on your marketplace website.
- [let isUpdate: Bool](installmetadata/isupdate.md)
  A Boolean value that indicates whether the installation is an app update.
- [let account: String](installmetadata/account.md)
  A user ID for the person installing the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installmetadata/alternativedistributionpackage)*