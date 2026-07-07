# missingPushExtension

**Framework**: Core Location  
**Kind**: property

An error code that indicates the app is missing a Location Push Service Extension.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
static var missingPushExtension: CLLocationPushServiceError.Code { get }
```

## See Also

- [static var unknown: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/unknown.md)
  An error code that indicates the app was unable to start the location push service for an unknown reason.
- [static var missingPushServerEnvironment: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingpushserverenvironment.md)
  An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [static var missingEntitlement: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingentitlement.md)
  An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [static var unsupportedPlatform: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.
- [CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/missingpushextension)*