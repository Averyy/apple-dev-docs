# FamilyControlsError.networkError

**Framework**: FamilyControls  
**Kind**: case

The device must be connected to the network in order to enroll with parental controls.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+

## Declaration

```swift
case networkError
```

## See Also

- [FamilyControlsError.invalidAccountType](familycontrolserror/invalidaccounttype.md)
  The device isn’t signed into a valid iCloud account.
- [FamilyControlsError.authorizationConflict](familycontrolserror/authorizationconflict.md)
  Another authorized app already provides parental controls.
- [FamilyControlsError.authorizationCanceled](familycontrolserror/authorizationcanceled.md)
  The parent or guardian canceled a request for authorization.
- [FamilyControlsError.invalidArgument](familycontrolserror/invalidargument.md)
  The method’s arguments are invalid.
- [FamilyControlsError.unavailable](familycontrolserror/unavailable.md)
  The system failed to set up the Family Control framework.
- [FamilyControlsError.restricted](familycontrolserror/restricted.md)
  A restriction prevents your app from using Family Controls on this device.
- [FamilyControlsError.authenticationMethodUnavailable](familycontrolserror/authenticationmethodunavailable.md)
  The device must have a passcode set in order for an individual to enroll with parental controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familycontrolserror/networkerror)*