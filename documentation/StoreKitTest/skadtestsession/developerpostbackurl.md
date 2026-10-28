# developerPostbackURL

**Framework**: StoreKit Test  
**Kind**: property  
**Role**: Instance Property

The URL that SKAdNetwork computes to send copies of winning postbacks to the advertised app’s developer.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var developerPostbackURL: URL? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSURL * developerPostbackURL;
```

## Discussion

Use this property to view the URL that [`SKAdNetwork`](../../StoreKit/skadnetwork.md) computes to send a copy of the winning postback to the developer. This property has a valid URL only if you specify a valid URL in the [`NSAdvertisingAttributionReportEndpoint`](../../BundleResources/information-property-list/nsadvertisingattributionreportendpoint.md) key in your app’s `Info.plist`. For more information, see [Configuring an advertised app](../../StoreKit/configuring-an-advertised-app.md).

> **Note**:  The testing environment doesn’t use this URL. [`SKAdNetwork`](../../StoreKit/skadnetwork.md) sends copies of winning postbacks in the production environment only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/skadtestsession/developerpostbackurl)*