# CLLocationPushServiceError.Code.missingPushServerEnvironment

**Framework**: Core Location  
**Kind**: case

An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
case missingPushServerEnvironment
```

#### Discussion

A Location Push Service Extension requires that your app has the APNs environment entitlement. For more information, see [`APS Environment Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/aps-environment).

## See Also

- [CLLocationPushServiceError.Code.unknown](cllocationpushserviceerror-swift.struct/code/unknown.md)
  An error code that indicates the app was unable to start the location push service for an unknown reason.
- [CLLocationPushServiceError.Code.missingPushExtension](cllocationpushserviceerror-swift.struct/code/missingpushextension.md)
  An error code that indicates the app is missing a Location Push Service Extension.
- [CLLocationPushServiceError.Code.missingEntitlement](cllocationpushserviceerror-swift.struct/code/missingentitlement.md)
  An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [CLLocationPushServiceError.Code.unsupportedPlatform](cllocationpushserviceerror-swift.struct/code/unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code/missingpushserverenvironment)*