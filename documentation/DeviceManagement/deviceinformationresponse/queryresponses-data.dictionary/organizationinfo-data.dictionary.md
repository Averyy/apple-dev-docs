# DeviceInformationResponse.QueryResponses.OrganizationInfo

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The response dictionary that contains organization information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object DeviceInformationResponse.QueryResponses.OrganizationInfo
```

## Properties

- `OrganizationAddress` (string): The organization’s address. Use the LF character (`&#10`) to insert line breaks.
- `OrganizationEmail` (string): The organization’s support email address.
- `OrganizationMagic` (string): A unique identifier for the various services a single organization manages.
- `OrganizationName` (string) *(required)*: A string that describes the organization operating the MDM server.
- `OrganizationPhone` (string): The organization’s phone number.

## See Also

### Objects
- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](./accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](./autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](./mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OSUpdateSettings](./osupdatesettings-data.dictionary.md)
  The response dictionary that contains operating system update settings.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](./servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.
- [object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings](./softwareupdatesettings-data.dictionary.md)
  The response dictionary that contains information about the Software Update pane in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/organizationinfo-data.dictionary)*