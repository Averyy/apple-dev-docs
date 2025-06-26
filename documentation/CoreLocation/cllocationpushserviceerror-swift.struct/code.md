# CLLocationPushServiceError.Code

**Framework**: Core Location  
**Kind**: enum

Error codes the location manager returns if starting to monitor for location push notifications fails.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
enum Code
```

#### Overview

These error codes are returned from [`startMonitoringLocationPushes(completion:)`](cllocationmanager/startmonitoringlocationpushes(completion:).md)

## Topics

### Getting the error code
- [CLLocationPushServiceError.Code.unknown](cllocationpushserviceerror-swift.struct/code/unknown.md)
  An error code that indicates the app was unable to start the location push service for an unknown reason.
- [CLLocationPushServiceError.Code.missingPushExtension](cllocationpushserviceerror-swift.struct/code/missingpushextension.md)
  An error code that indicates the app is missing a Location Push Service Extension.
- [CLLocationPushServiceError.Code.missingPushServerEnvironment](cllocationpushserviceerror-swift.struct/code/missingpushserverenvironment.md)
  An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [CLLocationPushServiceError.Code.missingEntitlement](cllocationpushserviceerror-swift.struct/code/missingentitlement.md)
  An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [CLLocationPushServiceError.Code.unsupportedPlatform](cllocationpushserviceerror-swift.struct/code/unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.
### Initializers
- [init?(rawValue: Int)](cllocationpushserviceerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Location Push Service Extension](../BundleResources/Entitlements/com.apple.developer.location.push.md)
  An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [protocol CLLocationPushServiceExtension](cllocationpushserviceextension.md)
  The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- [struct CLLocationPushServiceError](cllocationpushserviceerror-swift.struct.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.
- [let CLLocationPushServiceErrorDomain: String](cllocationpushserviceerrordomain.md)
  The domain for Location Push Service Extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code)*