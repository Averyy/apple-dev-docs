# ErrorCodePairingTokenMissing

**Framework**: Device Management  
**Kind**: dictionary

An error response that indicates a missing pairing token.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
object ErrorCodePairingTokenMissing
```

#### Discussion

The schema for a JSON or property list XML document that an MDM server’s 403 response body contains. The response headers need to include a “Content-Type” header that indicates whether the response returns JSON or XML.

The system returns this response when an Apple Watch enrolls in MDM, but the watch doesn’t include a `PAIRING_TOKEN` in the [`MachineInfo`](machineinfo.md) request. After the watch receives this response, it fetches a pairing token from the phone’s MDM server through a request to the phone. Then, the watch repeats the enrollment request and includes the pairing token.

## Topics

### Objects
- [object ErrorCodePairingTokenMissing.Details](errorcodepairingtokenmissing/details-data.dictionary.md)
  A dictionary that contains additional data about the token-missing error code.

## See Also

- [object ErrorCodePlatformSSORequired](errorcodeplatformssorequired.md)
  An error response that indicates Platform SSO is required.
- [object ErrorCodeSoftwareUpdateRequired](errorcodesoftwareupdaterequired.md)
  An error response that indicates the system requires a software update.
- [object ErrorUnrecognizedDevice](errorunrecognizeddevice.md)
  An error response that indicates a device needs to unenroll.
- [object ErrorWellKnownFailed](errorwellknownfailed.md)
  An error response that indicates a well-known service discovery request failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorcodepairingtokenmissing)*