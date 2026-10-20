# CLLocationPushServiceErrorDomain

**Framework**: Core Location  
**Kind**: var  
**Role**: Global Variable

The domain for Location Push Service Extension errors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
let CLLocationPushServiceErrorDomain: String
```

```c
extern NSErrorDomain const CLLocationPushServiceErrorDomain;
```

## See Also

### Location push service extension
- [Location Push Service Extension](../BundleResources/entitlements/com.apple.developer.location.push.md)
  An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [protocol CLLocationPushServiceExtension](./cllocationpushserviceextension.md)
  The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- [struct CLLocationPushServiceError](./cllocationpushserviceerror-swift.struct.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.
- [CLLocationPushServiceError.Code](./cllocationpushserviceerror-swift.struct/code.md)
  Error codes the location manager returns if starting to monitor for location push notifications fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationpushserviceerrordomain)*