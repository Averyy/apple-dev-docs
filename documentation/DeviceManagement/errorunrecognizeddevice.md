# ErrorUnrecognizedDevice

**Framework**: Device Management  
**Kind**: dictionary

An error response that indicates a device needs to unenroll.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ErrorUnrecognizedDevice
```

#### Discussion

The schema for a JSON or property list XML document that an MDM server’s 403 response body contains. The response headers need to include a “Content-Type” header that indicates whether the response returns JSON or XML.

The MDM server returns this response when it doesn’t recognize the device making the request. This causes the device to unenroll from the MDM server. Use this error instead of the server returning a 401 response to cause an unenroll.

## Properties

- `code` (string) *(required)*: Indicates that the device is not recognized by the server. This causes the device to unenroll from MDM.
- `description` (string): A description of the error. Only use this for logging purposes and don’t display it to the user.
- `message` (string): A description of the error to display to the user.

## See Also

- [object ErrorCodePairingTokenMissing](errorcodepairingtokenmissing.md)
  An error response that indicates a missing pairing token.
- [object ErrorCodePlatformSSORequired](errorcodeplatformssorequired.md)
  An error response that indicates Platform SSO is required.
- [object ErrorCodeSoftwareUpdateRequired](errorcodesoftwareupdaterequired.md)
  An error response that indicates the system requires a software update.
- [object ErrorWellKnownFailed](errorwellknownfailed.md)
  An error response that indicates a well-known service discovery request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorunrecognizeddevice)*