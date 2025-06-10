# CLLocationPushServiceError

**Framework**: Core Location  
**Kind**: struct

Error codes the location manager returns if starting to monitor for location push notifications fails.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
struct CLLocationPushServiceError
```

## Topics

### Getting the error code
- [static var unknown: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/unknown.md)
  An error code that indicates the app was unable to start the location push service for an unknown reason.
- [static var missingPushExtension: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingpushextension.md)
  An error code that indicates the app is missing a Location Push Service Extension.
- [static var missingPushServerEnvironment: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingpushserverenvironment.md)
  An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [static var missingEntitlement: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/missingentitlement.md)
  An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [static var unsupportedPlatform: CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.
- [CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.
### Type Properties
- [static var errorDomain: String](cllocationpushserviceerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [com.apple.developer.location.push](../BundleResources/Entitlements/com.apple.developer.location.push.md)
  An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [protocol CLLocationPushServiceExtension](cllocationpushserviceextension.md)
  The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- [let CLLocationPushServiceErrorDomain: String](cllocationpushserviceerrordomain.md)
  The domain for Location Push Service Extension errors.
- [CLLocationPushServiceError.Code](cllocationpushserviceerror-swift.struct/code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct)*