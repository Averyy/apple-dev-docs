# ATTrackingManager.AuthorizationStatus.restricted

**Framework**: App Tracking Transparency  
**Kind**: case  
**Role**: Case

A value that indicates the system restricts tracking authorization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case restricted
```

```c
ATTrackingManagerAuthorizationStatusRestricted
```

#### Discussion

When the system restricts tracking for the device:

- Tracking request methods (for example, [`requestTrackingAuthorization(completionHandler:)`](../requesttrackingauthorization%28completionhandler%29.md)) run their completion handlers immediately, without prompting the person.
- The system disables “Allow Apps to Request to Track” (called “Allow Apps to Request to Link Your Activity Across Companies” in the European Union) in Settings > Privacy & Security > Tracking.

## See Also

### Determining the status
- [ATTrackingManager.AuthorizationStatus.authorized](./authorized.md)
  A value that indicates someone grants your app permission to access data your app can use to track a person or device.
- [ATTrackingManager.AuthorizationStatus.denied](./denied.md)
  A value that indicates someone denies your app permission to access data your app can use to track a person or device.
- [ATTrackingManager.AuthorizationStatus.notDetermined](./notdetermined.md)
  A value that indicates the person hasn’t responded to a tracking authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus/restricted)*