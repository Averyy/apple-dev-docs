# developerPostbackURL

**Framework**: StoreKit Test  
**Kind**: property

The URL that SKAdNetwork computes to send copies of winning postbacks to the advertised app’s developer.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var developerPostbackURL: URL? { get }
```

#### Discussion

Use this property to view the URL that [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) computes to send a copy of the winning postback to the developer. This property has a valid URL only if you specify a valid URL in the [`NSAdvertisingAttributionReportEndpoint`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAdvertisingAttributionReportEndpoint) key in your app’s `Info.plist`. For more information, see [`Configuring an advertised app`](https://developer.apple.com/documentation/StoreKit/configuring-an-advertised-app).

> **Note**:  The testing environment doesn’t use this URL. [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) sends copies of winning postbacks in the production environment only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/developerpostbackurl)*