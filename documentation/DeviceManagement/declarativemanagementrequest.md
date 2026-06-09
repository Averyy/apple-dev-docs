# DeclarativeManagementRequest

**Framework**: Device Management  
**Kind**: dictionary

The declarative management request details.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object DeclarativeManagementRequest
```

## Topics

### Declaration Endpoints
- [declaration/activation/{identifier}](declaration-activation-_identifier_.md)
  The endpoint for fetching an activation declaration.
- [declaration/asset/{identifier}](declaration-asset-_identifier_.md)
  The endpoint for fetching an asset declaration.
- [declaration/configuration/{identifier}](declaration-configuration-_identifier_.md)
  The endpoint for fetching a configuration declaration.
- [declaration/management/{identifier}](declaration-management-_identifier_.md)
  The endpoint for fetching a management declaration.
### Declaration Response
- [object DeclarationResponse](declarationresponse.md)

## Properties

- `Data` (data): A Base64-encoded JSON object using the [`SynchronizationTokens`](synchronizationtokens.md) schema.
- `Endpoint` (string) *(required)*: The type of operation the declaration is requesting. This key needs to be one of these values: - `tokens`: For fetching synchronization tokens from the server
- `declaration-items`: For fetching the declaration manifest from the server
- `status`: For sending a status report to the server
- `declaration/…/…`: For fetching a specific declaration from the server. Include the declaration type and identifier separated by slash characters (`/`).
- `EnrollmentID` (string) *(required)*: The per-enrollment identifier for the device. The system requires this value if the enrollment type is a user enrollment. Available: iOS 15+ | iPadOS 15+ | macOS 13+ | visionOS 1.1+
- `EnrollmentUserID` (string) *(required)*: The per-enrollment identifier for the user. The system requires this value if the enrollment type is a user enrollment on the user channel. Available: macOS 13+
- `MessageType` (string) *(required)*: The message type, which requires a value of `DeclarativeManagement`.
- `UDID` (string) *(required)*: The device’s UDID (unique device identifier). The system requires this value if the enrollment type is a device enrollment.
- `UserID` (string): For macOS, this value is the ID of the user. For Shared iPad, this value is `FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF` to indicate that authentication doesn’t occur. Available: iOS 15+ | iPadOS 15+ | macOS 13+
- `UserLongName` (string) *(required)*: The full name of the user. Available: macOS 13+
- `UserShortName` (string): For macOS, this value is the short name of the user. For Shared iPad, this value is the Managed Apple Account identifier of the user on Shared iPad. It indicates that the token is for the user channel. Available: iOS 15+ | iPadOS 15+ | macOS 13+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarativemanagementrequest)*