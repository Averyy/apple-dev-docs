# FamilyControlsError

**Framework**: FamilyControls  
**Kind**: enum

Errors the Family Controls framework reports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+

## Declaration

```swift
enum FamilyControlsError
```

## Topics

### Error Values
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
- [FamilyControlsError.networkError](familycontrolserror/networkerror.md)
  The device must be connected to the network in order to enroll with parental controls.
- [FamilyControlsError.authenticationMethodUnavailable](familycontrolserror/authenticationmethodunavailable.md)
  The device must have a passcode set in order for an individual to enroll with parental controls.
### Error Data
- [var errorDescription: String?](familycontrolserror/errordescription.md)
  A nonlocalized description of the error, suitable for debugging.
- [var errorDescription: String?](familycontrolserror/errordescription.md)
  A nonlocalized description of the error, suitable for debugging.
- [var localizedDescription: String](familycontrolserror/localizeddescription.md)
  Retrieve the localized description for this error.
- [var failureReason: String?](familycontrolserror/failurereason.md)
  A localized message describing the reason for the failure.
- [var recoverySuggestion: String?](familycontrolserror/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.
- [var helpAnchor: String?](familycontrolserror/helpanchor.md)
  A localized message providing “help” text if the user requests help.
### Comparisons
- [static func != (Self, Self) -> Bool](familycontrolserror/!=(_:_:).md)
  Returns a Boolean value that indicates whether two error values aren’t equal.
- [func hash(into: inout Hasher)](familycontrolserror/hash(into:).md)
- [var hashValue: Int](familycontrolserror/hashvalue.md)
### Default Implementations
- [CustomNSError Implementations](familycontrolserror/customnserror-implementations.md)
- [Equatable Implementations](familycontrolserror/equatable-implementations.md)
- [Error Implementations](familycontrolserror/error-implementations.md)
- [LocalizedError Implementations](familycontrolserror/localizederror-implementations.md)
- [RawRepresentable Implementations](familycontrolserror/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familycontrolserror)*