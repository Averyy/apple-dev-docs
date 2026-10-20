# authorizationStatus()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

Returns the authorization status for monitoring headphone motion.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 14.0+
- watchOS 7.0+

## Declaration

```swift
class func authorizationStatus() -> CMAuthorizationStatus
```

```objc
+ (CMAuthorizationStatus) authorizationStatus;
```

## See Also

### Checking Availability
- [var isDeviceMotionAvailable: Bool](./isdevicemotionavailable.md)
  A Boolean value that indicates whether the current device supports the headphone motion manager.
- [var isDeviceMotionActive: Bool](./isdevicemotionactive.md)
  A Boolean value that indicates whether the headphone motion manager is active.
- [var isConnectionStatusActive: Bool](./isconnectionstatusactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphonemotionmanager/authorizationstatus())*