# ErrorCodeSoftwareUpdateRequired

**Framework**: Device Management  
**Kind**: dictionary

An error response that indicates the system requires a software update.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS 26.0+ (Beta)

## Declaration

```swift
object ErrorCodeSoftwareUpdateRequired
```

#### Discussion

The MDM server’s 403 response body contains the schema for a JSON or property list XML document. The response headers need to include a “Content-Type” header that indicates whether the response returns JSON or XML.

The system returns this response when a device attempts to enroll with an MDM server during Setup Assistant, but the MDM server requires the device to perform a software update before it can continue with enrollment and setup.

## Topics

### Objects
- [object ErrorCodeSoftwareUpdateRequired.Details](errorcodesoftwareupdaterequired/details-data.dictionary.md)
  A dictionary that contains additional data about the software update required error code.

## See Also

- [object ErrorCodePairingTokenMissing](errorcodepairingtokenmissing.md)
  An error response that indicates a missing pairing token.
- [object ErrorUnrecognizedDevice](errorunrecognizeddevice.md)
- [object ErrorWellKnownFailed](errorwellknownfailed.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorcodesoftwareupdaterequired)*