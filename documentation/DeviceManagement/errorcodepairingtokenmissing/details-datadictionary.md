# ErrorCodePairingTokenMissing.Details

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that contains additional data about the token-missing error code.

**Availability**:
- watchOS 10.0+

## Declaration

```swift
object ErrorCodePairingTokenMissing.Details
```

## Properties

- `security-token` (string) *(required)*: The security token to pass to the phone’s MDM server to create the pairing token. This token needs to be a random UUID string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorcodepairingtokenmissing/details-data.dictionary)*