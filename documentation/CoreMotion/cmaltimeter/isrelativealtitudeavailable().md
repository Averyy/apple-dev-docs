# isRelativeAltitudeAvailable()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value indicating whether the current device supports generating data for relative altitude changes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class func isRelativeAltitudeAvailable() -> Bool
```

```objc
+ (BOOL) isRelativeAltitudeAvailable;
```

## Return Value

[`true`](../../Swift/true.md) if the device supports relative altitude changes or [`false`](../../Swift/false.md) if it does not.

## Discussion

Use this method to determine if altitude updates are available before calling the [`startRelativeAltitudeUpdates(to:withHandler:)`](./startrelativealtitudeupdates%28to,withhandler%29.md) method.

## See Also

### Determining Altitude Availability
- [class func isAbsoluteAltitudeAvailable() -> Bool](./isabsolutealtitudeavailable%28%29.md)
  Returns a Boolean value indicating whether the current device reports changes in the absolute altitude.
- [class func authorizationStatus() -> CMAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns a value indicating whether the app is authorized to retrieve altimeter data.
- [enum CMAuthorizationStatus](../cmauthorizationstatus.md)
  The authorization status for motion-related features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmaltimeter/isrelativealtitudeavailable())*