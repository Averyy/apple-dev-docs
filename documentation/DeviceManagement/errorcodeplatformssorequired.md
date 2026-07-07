# ErrorCodePlatformSSORequired

**Framework**: Device Management  
**Kind**: dictionary

An error response that indicates Platform SSO is required.

**Availability**:
- macOS 26.0+

## Declaration

```swift
object ErrorCodePlatformSSORequired
```

## Mentions

- [Implementing Platform SSO during Automated Device Enrollment](implementing-platform-sso-during-automated-device-enrollment.md)

#### Discussion

The schema for a JSON or property list XML document that an MDM server’s 403 response body contains. The response headers need to include a “Content-Type” header that indicates whether the response returns JSON or XML.

The MDM server returns this response when a device enrolls in MDM during Setup Assistant and it requires the user to sign-in using Platform SSO before it allows enrollment and setup to proceed.

## Topics

### Objects
- [object ErrorCodePlatformSSORequired.Details](errorcodeplatformssorequired/details-data.dictionary.md)
  A dictionary that contains additional data about the error code.

## Properties

- `code` (string) *(required)*: Indicates that the device needs to do Platform SSO before enrollment and setup can proceed.
- `description` (string): A description of the error. Only use this for logging purposes and don’t display it to the user.
- `details` (ErrorCodePlatformSSORequired.Details) *(required)*: A dictionary that contains additional data about the error code.
- `message` (string): A description of the error to display to the user.

## See Also

- [object ErrorCodePairingTokenMissing](errorcodepairingtokenmissing.md)
  An error response that indicates a missing pairing token.
- [object ErrorCodeSoftwareUpdateRequired](errorcodesoftwareupdaterequired.md)
  An error response that indicates the system requires a software update.
- [object ErrorUnrecognizedDevice](errorunrecognizeddevice.md)
  An error response that indicates a device needs to unenroll.
- [object ErrorWellKnownFailed](errorwellknownfailed.md)
  An error response that indicates a well-known service discovery request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorcodeplatformssorequired)*