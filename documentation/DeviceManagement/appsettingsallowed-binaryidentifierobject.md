# AppSettingsAllowed_BinaryIdentifierObject

**Framework**: Device Management  
**Kind**: dictionary

Dictionary containing one or more identifier fields to match a binary.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object AppSettingsAllowed_BinaryIdentifierObject
```

## Properties

- `CDHash` (string): The code signature code directory hash of the binary.
- `PathPrefix` (string): The file system path prefix to match binaries.
- `SigningID` (string): The code signature signing identifier of the binary.
- `SigningState` (string): The code signing state to match binaries.
- `TeamID` (string): The code signature team identifier of the binary. Use the value “*APPLE*” instead of an empty string for Apple binaries with an empty team identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/appsettingsallowed_binaryidentifierobject)*