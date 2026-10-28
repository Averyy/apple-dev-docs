# account

**Framework**: MarketplaceKit  
**Kind**: property  
**Role**: Instance Property

A user ID for the person installing the app.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let account: String
```

## Discussion

You set this value and the operating system sends it back to you as:

- The `login_hint` in the call to your authorization endpoint during re-authentication
- A parameter to your marketplace extension’s [`additionalHeaders(for:account:)`](../marketplaceappextension/additionalheaders%28for,account%29.md) callback

The system also groups apps in restore requests based on account.

## See Also

### Inspecting app and account information
- [let appleItemID: AppleItemID](./appleitemid.md)
  A unique identifier for the app to install.
- [let alternativeDistributionPackage: URL](./alternativedistributionpackage.md)
  A URL to the app’s assembled alternative distribution package.
- [var appShareURL: URL?](./appshareurl.md)
  A URL to a product landing page for the app on your marketplace website.
- [let isUpdate: Bool](./isupdate.md)
  A Boolean value that indicates whether the installation is an app update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installmetadata/account)*