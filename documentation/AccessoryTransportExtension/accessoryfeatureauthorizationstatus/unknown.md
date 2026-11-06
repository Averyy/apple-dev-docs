# AccessoryFeatureAuthorizationStatus.unknown

**Framework**: Accessory Transport Extension  
**Kind**: case  
**Role**: Case

A value that indicates the system doesn’t have an authorization record for the accessory feature.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
case unknown
```

## Discussion

Enroll a feature by using `AccessoryWorker/requestAuthorization(for:)` or `AccessoryGPUWorker/requestAuthorization(for:)`.

## See Also

### Determining the authorization status
- [AccessoryFeatureAuthorizationStatus.unauthorized](./unauthorized.md)
  A value that indicates your extension hasn’t authorized the feature.
- [AccessoryFeatureAuthorizationStatus.authorized](./authorized.md)
  A value that indicates your extension authorizes the feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureauthorizationstatus/unknown)*