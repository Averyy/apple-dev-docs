# ErrorCodeSoftwareUpdateRequired

**Framework**: Device Management  
**Kind**: dictionary

An error response that indicates the system requires a software update.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS 26.0+

## Declaration

```swift
object ErrorCodeSoftwareUpdateRequired
```

## Mentions

- [Returning a managed device to service](returning-a-managed-device-to-service.md)

#### Discussion

The schema for a JSON or property list XML document that an MDM server’s 403 response body contains. The response headers need to include a “Content-Type” header that indicates whether the response returns JSON or XML.

The MDM server returns this response when a device enrolls in MDM during Setup Assistant and it requires the device to perform a software update before it can continue with enrollment and setup.

## Topics

### Objects
- [object ErrorCodeSoftwareUpdateRequired.Details](errorcodesoftwareupdaterequired/details-data.dictionary.md)
  A dictionary that contains additional data about the software update required error code.

## See Also

- [object ErrorCodePairingTokenMissing](errorcodepairingtokenmissing.md)
  An error response that indicates a missing pairing token.
- [object ErrorCodePlatformSSORequired](errorcodeplatformssorequired.md)
  An error response that indicates Platform SSO is required.
- [object ErrorUnrecognizedDevice](errorunrecognizeddevice.md)
  An error response that indicates a device needs to unenroll.
- [object ErrorWellKnownFailed](errorwellknownfailed.md)
  An error response that indicates a well-known service discovery request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorcodesoftwareupdaterequired)*