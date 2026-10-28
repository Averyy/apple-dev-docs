# FamilyControlsError.invalidAccountType

**Framework**: Family Controls  
**Kind**: case  
**Role**: Case

The device isn’t signed into a valid iCloud account.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+

## Declaration

```swift
case invalidAccountType
```

## Discussion

To request or revoke authorization, the user must sign into iCloud from a child account that’s part of a Family Sharing group.

## See Also

### Error values
- [FamilyControlsError.authorizationConflict](./authorizationconflict.md)
  Another authorized app already provides parental controls.
- [FamilyControlsError.authorizationCanceled](./authorizationcanceled.md)
  The parent or guardian canceled a request for authorization.
- [FamilyControlsError.invalidArgument](./invalidargument.md)
  The method’s arguments are invalid.
- [FamilyControlsError.unavailable](./unavailable.md)
  The system failed to set up the Family Control framework.
- [FamilyControlsError.restricted](./restricted.md)
  A restriction prevents your app from using Family Controls on this device.
- [FamilyControlsError.networkError](./networkerror.md)
  The device must be connected to the network in order to enroll with parental controls.
- [FamilyControlsError.authenticationMethodUnavailable](./authenticationmethodunavailable.md)
  The device must have a passcode set in order for an individual to enroll with parental controls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familycontrolserror/invalidaccounttype)*