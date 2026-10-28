# CLLocationPushServiceError.Code

**Framework**: Core Location  
**Kind**: enum  
**Role**: Enumeration

Error codes the location manager returns if starting to monitor for location push notifications fails.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum Code
```

```c
enum CLLocationPushServiceError : NSInteger;
```

## Overview

These error codes are returned from [`startMonitoringLocationPushes(completion:)`](../cllocationmanager/startmonitoringlocationpushes%28completion%29.md)

## Topics

### Getting the error code
- [CLLocationPushServiceError.Code.unknown](./code/unknown.md)
  An error code that indicates the app was unable to start the location push service for an unknown reason.
- [CLLocationPushServiceError.Code.missingPushExtension](./code/missingpushextension.md)
  An error code that indicates the app is missing a Location Push Service Extension.
- [CLLocationPushServiceError.Code.missingPushServerEnvironment](./code/missingpushserverenvironment.md)
  An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [CLLocationPushServiceError.Code.missingEntitlement](./code/missingentitlement.md)
  An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [CLLocationPushServiceError.Code.unsupportedPlatform](./code/unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Location push service extension
- [Location Push Service Extension](../../BundleResources/entitlements/com.apple.developer.location.push.md)
  An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [protocol CLLocationPushServiceExtension](../cllocationpushserviceextension.md)
  The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- [struct CLLocationPushServiceError](../cllocationpushserviceerror-swift.struct.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.
- [let CLLocationPushServiceErrorDomain: String](../cllocationpushserviceerrordomain.md)
  The domain for Location Push Service Extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code)*