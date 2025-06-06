# missingPushServerEnvironment

**Framework**: Core Location  
**Kind**: property

An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
static var missingPushServerEnvironment: CLLocationPushServiceError.Code { get }
```

#### Discussion

A Location Push Service Extension requires that your app has the APNs environment entitlement. For more information, see [`APS Environment Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/aps-environment).

## See Also

- [static var unknown: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/unknown.md)
  An error code that indicates the app was unable to start the location push service for an unknown reason.
- [static var missingPushExtension: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingpushextension.md)
  An error code that indicates the app is missing a Location Push Service Extension.
- [static var missingEntitlement: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingentitlement.md)
  An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [static var unsupportedPlatform: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.
- [CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/missingpushserverenvironment)*