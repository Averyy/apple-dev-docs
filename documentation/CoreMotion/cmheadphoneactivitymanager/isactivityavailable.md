# isActivityAvailable

**Framework**: Core Motion  
**Kind**: property

A Boolean value that indicates whether the current device supports headphone activity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- watchOS 11.0+

## Declaration

```swift
var isActivityAvailable: Bool { get }
```

#### Discussion

If the device supports headphone activity, start status updates and then wait for an update that indicates supported headphones are connected.

## See Also

- [var isActivityActive: Bool](cmheadphoneactivitymanager/isactivityactive.md)
  A Boolean value that indicates whether headphone motion activity is active.
- [var isStatusAvailable: Bool](cmheadphoneactivitymanager/isstatusavailable.md)
  A Boolean value that indicates whether the current device supports headphone status.
- [var isStatusActive: Bool](cmheadphoneactivitymanager/isstatusactive.md)
  A Boolean value that indicates whether headphone status is active.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmheadphoneactivitymanager/authorizationstatus.md)
  Returns the authorization status for monitoring headphone activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmheadphoneactivitymanager/isactivityavailable)*