# missingEntitlement

**Framework**: Core Location  
**Kind**: property

An error code that indicates the app is missing the entitlement it needs to use the location push service.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
static var missingEntitlement: CLLocationPushServiceError.Code { get }
```

#### Discussion

For more information, see [`Creating a location push service extension`](creating-a-location-push-service-extension.md).

## See Also

- [static var unknown: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/unknown.md)
  An error code that indicates the app was unable to start the location push service for an unknown reason.
- [static var missingPushExtension: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingpushextension.md)
  An error code that indicates the app is missing a Location Push Service Extension.
- [static var missingPushServerEnvironment: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingpushserverenvironment.md)
  An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [static var unsupportedPlatform: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.
- [CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/missingentitlement)*