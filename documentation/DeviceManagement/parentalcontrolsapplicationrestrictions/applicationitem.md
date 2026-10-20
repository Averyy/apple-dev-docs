# ParentalControlsApplicationRestrictions.ApplicationItem

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

A dictionary defining an app for parental control.

**Availability**:
- macOS 10.15+ - Deprecated in 27.0

> **Deprecated**: Use the declarative management `com.apple.configuration.app.settings` configuration.

## Declaration

```
object ParentalControlsApplicationRestrictions.ApplicationItem
```

## Properties

- `appID` (data) *(required)* *(deprecated)*: The identifier of the app. Obtain this value from the Security framework using [`SecCodeCopyDesignatedRequirement(_:_:_:)`](../../Security/seccodecopydesignatedrequirement%28_,_,_%29.md).

  Deprecated: macOS 27+
- `bundleID` (string) *(required)* *(deprecated)*: The bundle ID of the app.

  Deprecated: macOS 27+
- `detachedSignature` (data) *(deprecated)*: The signature for an unsigned binary.

  Deprecated: macOS 27+
- `disabled` (boolean) *(deprecated)*: If `true`, this app isn’t added to the allow list.

  Deprecated: macOS 27+

  **Default**: `false`
- `displayName` (string) *(deprecated)*: The name used for display purposes.

  Deprecated: macOS 27+
- `subApps` ([ParentalControlsApplicationRestrictions.ApplicationItem]) *(deprecated)*: An array of nested helper applications.

  Deprecated: macOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsapplicationrestrictions/applicationitem)*