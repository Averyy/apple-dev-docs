# ParentalControlsApplicationRestrictions.ApplicationItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary defining an app for parental control.

**Availability**:
- macOS 10.15+

## Declaration

```swift
object ParentalControlsApplicationRestrictions.ApplicationItem
```

## Properties

- `appID` (data) *(required)*: The identifier of the app. Obtain this value from the Security framework using [`SecCodeCopyDesignatedRequirement(_:_:_:)`](https://developer.apple.com/documentation/Security/SecCodeCopyDesignatedRequirement(_:_:_:)). Deprecated: macOS 27+
- `bundleID` (string) *(required)*: The bundle ID of the app. Deprecated: macOS 27+
- `detachedSignature` (data): The signature for an unsigned binary. Deprecated: macOS 27+
- `disabled` (boolean): If `true`, this app isn’t added to the allow list. Deprecated: macOS 27+
- `displayName` (string): The name used for display purposes. Deprecated: macOS 27+
- `subApps` ([ParentalControlsApplicationRestrictions.ApplicationItem]): An array of nested helper applications. Deprecated: macOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsapplicationrestrictions/applicationitem)*