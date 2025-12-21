# ErrorWellKnownFailed

**Framework**: Device Management  
**Kind**: dictionary

An error response that indicates a well-known service discovery request failed.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- macOS 14.5+
- visionOS 1.2+

## Declaration

```swift
object ErrorWellKnownFailed
```

#### Discussion

The schema for a JSON or property list XML document that an MDM server’s 403 response body contains. The response headers need to include a “Content-Type” header that indicates whether the response returns JSON or XML.

The MDM server returns this response to reject a well-known service discovery request from a device made during an account driven enrollment.

## See Also

- [object ErrorCodePairingTokenMissing](errorcodepairingtokenmissing.md)
  An error response that indicates a missing pairing token.
- [object ErrorCodePlatformSSORequired](errorcodeplatformssorequired.md)
  An error response that indicates Platform SSO is required.
- [object ErrorCodeSoftwareUpdateRequired](errorcodesoftwareupdaterequired.md)
  An error response that indicates the system requires a software update.
- [object ErrorUnrecognizedDevice](errorunrecognizeddevice.md)
  An error response that indicates a device needs to unenroll.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorwellknownfailed)*