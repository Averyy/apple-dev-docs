# authorizationStatus()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

Returns a value indicating whether the app is authorized to retrieve altimeter data.

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

### Determining Altitude Availability
- [class func isAbsoluteAltitudeAvailable() -> Bool](./isabsolutealtitudeavailable%28%29.md)
  Returns a Boolean value indicating whether the current device reports changes in the absolute altitude.
- [class func isRelativeAltitudeAvailable() -> Bool](./isrelativealtitudeavailable%28%29.md)
  Returns a Boolean value indicating whether the current device supports generating data for relative altitude changes.
- [enum CMAuthorizationStatus](../cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter/authorizationstatus())*