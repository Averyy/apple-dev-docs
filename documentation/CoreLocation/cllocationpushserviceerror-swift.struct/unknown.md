# unknown

**Framework**: Core Location  
**Kind**: property  
**Role**: Type Property

An error code that indicates the app was unable to start the location push service for an unknown reason.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
static var unknown: CLLocationPushServiceError.Code { get }
```

## See Also

### Getting the error code
- [static var missingPushExtension: CLLocationPushServiceError.Code](./missingpushextension.md)
  An error code that indicates the app is missing a Location Push Service Extension.
- [static var missingPushServerEnvironment: CLLocationPushServiceError.Code](./missingpushserverenvironment.md)
  An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [static var missingEntitlement: CLLocationPushServiceError.Code](./missingentitlement.md)
  An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [static var unsupportedPlatform: CLLocationPushServiceError.Code](./unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.
- [CLLocationPushServiceError.Code](./code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/unknown)*