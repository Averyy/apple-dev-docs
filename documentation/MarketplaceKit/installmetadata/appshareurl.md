# appShareURL

**Framework**: MarketplaceKit  
**Kind**: property  
**Role**: Instance Property

A URL to a product landing page for the app on your marketplace website.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var appShareURL: URL?
```

## Discussion

The operating system populates the value in the Share Sheet when a person touches and holds the app’s icon on the Home Screen.

## See Also

### Inspecting app and account information
- [let appleItemID: AppleItemID](./appleitemid.md)
  A unique identifier for the app to install.
- [let alternativeDistributionPackage: URL](./alternativedistributionpackage.md)
  A URL to the app’s assembled alternative distribution package.
- [let isUpdate: Bool](./isupdate.md)
  A Boolean value that indicates whether the installation is an app update.
- [let account: String](./account.md)
  A user ID for the person installing the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installmetadata/appshareurl)*