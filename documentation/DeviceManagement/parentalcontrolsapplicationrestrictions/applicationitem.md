# ParentalControlsApplicationRestrictions.ApplicationItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary defining an app for parental control.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object ParentalControlsApplicationRestrictions.ApplicationItem
```

## Properties

- `appID` (data) *(required)*: The identifier of the app. Obtain this value from the Security framework using [`SecCodeCopyDesignatedRequirement(_:_:_:)`](https://developer.apple.com/documentation/Security/SecCodeCopyDesignatedRequirement(_:_:_:)).
- `bundleID` (string) *(required)*: The bundle ID of the app.
- `detachedSignature` (data): The signature for an unsigned binary.
- `disabled` (boolean): If `true`, this app isn’t added to the allow list.
- `displayName` (string): The name used for display purposes.
- `subApps` ([ParentalControlsApplicationRestrictions.ApplicationItem]): An array of nested helper applications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsapplicationrestrictions/applicationitem)*