# CLLocationPushServiceError.Code.missingPushExtension

**Framework**: Core Location  
**Kind**: case  
**Role**: Case

An error code that indicates the app is missing a Location Push Service Extension.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case missingPushExtension
```

```c
CLLocationPushServiceErrorMissingPushExtension
```

## Discussion

For more information, see [Creating a location push service extension](../../creating-a-location-push-service-extension.md).

## See Also

### Getting the error code
- [CLLocationPushServiceError.Code.unknown](./unknown.md)
  An error code that indicates the app was unable to start the location push service for an unknown reason.
- [CLLocationPushServiceError.Code.missingPushServerEnvironment](./missingpushserverenvironment.md)
  An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [CLLocationPushServiceError.Code.missingEntitlement](./missingentitlement.md)
  An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [CLLocationPushServiceError.Code.unsupportedPlatform](./unsupportedplatform.md)
  An error code that indicates the location push service isn’t available on this platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code/missingpushextension)*