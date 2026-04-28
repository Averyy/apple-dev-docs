# ProfileListResponse.ProfileListItem

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that describes a profile list item.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ProfileListResponse.ProfileListItem
```

## Mentions

- [Dealing with Inactive MDM Devices and Invalid Push Tokens](dealing-with-inactive-mdm-devices-and-invalid-push-tokens.md)

## Topics

### Objects
- [object ProfileListResponse.ProfileListItem.PayloadContentItem](profilelistresponse/profilelistitem/payloadcontentitem.md)
  A dictionary that describes a profile payload content item.

## Properties

- `HasRemovalPasscode` (boolean): If `true`, the profile has a passcode for removal.
- `IsEncrypted` (boolean): If `true`, it’s an encrypted profile.
- `IsManaged` (boolean): If `true`, the current MDM service installed the profile. MDM doesn’t return this value for supervised devices, and can remove or replace all profiles on supervised devices.
- `PayloadContent` ([ProfileListResponse.ProfileListItem.PayloadContentItem]): An array of payload content items. This value isn’t present if `IsEncrypted` is `true`.
- `PayloadDescription` (string): The description of the profile.
- `PayloadDisplayName` (string): The human-readable name of the profile.
- `PayloadIdentifier` (string) *(required)*: The reverse-DNS-style identifier of the profile; for example, `com.example.myprofile`.
- `PayloadOrganization` (string): The human-readable name of the organization that provided the profile.
- `PayloadRemovalDisallowed` (boolean): If `true`, the user can’t delete the profile unless it has a removal password and the user provides it. The framework ignores this field on unsupervised devices.
- `PayloadUUID` (string) *(required)*: The unique identifier for the profile.
- `PayloadVersion` (integer): The version of the configuration profile as a whole, not of the individual profiles within it. The value should be `1`.
- `SignerCertificates` ([data]): An array that contains the certificate for signing the profile, followed by any intermediate certificates, in DER-encoded X.509 format.
- `Source` (string): A string set to `Declarative Device Management` when the profile is managed by Declarative Device Management.

## See Also

- [object ProfileListResponse.ErrorChainItem](profilelistresponse/errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profilelistresponse/profilelistitem)*