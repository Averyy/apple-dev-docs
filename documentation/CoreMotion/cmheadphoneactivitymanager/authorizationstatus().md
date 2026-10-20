# authorizationStatus()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

Returns the authorization status for monitoring headphone activity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
class func authorizationStatus() -> CMAuthorizationStatus
```

```objc
+ (CMAuthorizationStatus) authorizationStatus;
```

## See Also

### Checking Availability
- [var isActivityAvailable: Bool](./isactivityavailable.md)
  A Boolean value that indicates whether the current device supports headphone activity.
- [var isActivityActive: Bool](./isactivityactive.md)
  A Boolean value that indicates whether headphone motion activity is active.
- [var isStatusAvailable: Bool](./isstatusavailable.md)
  A Boolean value that indicates whether the current device supports headphone status.
- [var isStatusActive: Bool](./isstatusactive.md)
  A Boolean value that indicates whether headphone status is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/authorizationstatus())*