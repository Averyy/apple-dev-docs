# authorizationStatus()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

Returns a value indicating whether the app is authorized to retrieve stored motion data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- watchOS 4.0+

## Declaration

```swift
class func authorizationStatus() -> CMAuthorizationStatus
```

```objc
+ (CMAuthorizationStatus) authorizationStatus;
```

## See Also

### Determining Activity Availability
- [class func isActivityAvailable() -> Bool](./isactivityavailable%28%29.md)
  Returns a Boolean indicating whether motion data is available on the current device.
- [enum CMAuthorizationStatus](../cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/authorizationstatus())*