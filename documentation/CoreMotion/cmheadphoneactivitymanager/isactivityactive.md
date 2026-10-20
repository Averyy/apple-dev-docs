# isActivityActive

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether headphone motion activity is active.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
var isActivityActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isActivityActive) BOOL activityActive;
```

## See Also

### Checking Availability
- [var isActivityAvailable: Bool](./isactivityavailable.md)
  A Boolean value that indicates whether the current device supports headphone activity.
- [var isStatusAvailable: Bool](./isstatusavailable.md)
  A Boolean value that indicates whether the current device supports headphone status.
- [var isStatusActive: Bool](./isstatusactive.md)
  A Boolean value that indicates whether headphone status is active.
- [class func authorizationStatus() -> CMAuthorizationStatus](./authorizationstatus%28%29.md)
  Returns the authorization status for monitoring headphone activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityactive)*