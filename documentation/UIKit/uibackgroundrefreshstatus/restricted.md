# UIBackgroundRefreshStatus.restricted

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

Background updates are unavailable and the user cannot enable them again.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case restricted
```

```c
UIBackgroundRefreshStatusRestricted
```

## Discussion

For example, this status can occur when parental controls are in effect for the current user.

## See Also

### Constants
- [UIBackgroundRefreshStatus.denied](./denied.md)
  The user explicitly disabled background behavior for this app or for the whole system.
- [UIBackgroundRefreshStatus.available](./available.md)
  Background updates are available for the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundrefreshstatus/restricted)*