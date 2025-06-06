# InstallRequirements

**Framework**: MarketplaceKit  
**Kind**: struct

An app’s installation criteria for a device.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct InstallRequirements
```

## Topics

### Initializers
- [init()](installrequirements/init.md)
- [init(from: any Decoder) throws](installrequirements/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var ageRatingRank: Int?](installrequirements/ageratingrank.md)
- [var expectedInstallSize: UInt64?](installrequirements/expectedinstallsize.md)
- [var minimumSystemVersion: String?](installrequirements/minimumsystemversion.md)
  A text representation of the system version required to install an app.
- [var requiredDeviceCapabilities: Set<String>?](installrequirements/requireddevicecapabilities.md)
  The capabilities that a device requires to install an app.
### Instance Methods
- [func encode(to: any Encoder) throws](installrequirements/encode(to:).md)
  Encodes this value into the given encoder.
- [func satisfiedByDevice() -> Bool](installrequirements/satisfiedbydevice.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AppLibrary](applibrary.md)
  An object that manages search characteristics, licensing, and the installation of apps.
- [struct AppVersion](appversion.md)
  Information that describes an app, including its identifier and version number.
- [struct AutomaticUpdate](automaticupdate.md)
  Information that describes an app that’s available for update, including a download URL.
- [typealias AppleItemID](appleitemid.md)
  An identifier that represents an app.
- [typealias AppleVersionID](appleversionid.md)
  An identifier that represents a single app version.
- [let MarketplaceKitURIScheme: String](marketplacekiturischeme.md)
  A URI scheme that defines an alternative distribution app installation link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/installrequirements)*