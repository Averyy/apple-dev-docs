# DeviceInformationResponse.QueryResponses.OrganizationInfo

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that contains organization information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DeviceInformationResponse.QueryResponses.OrganizationInfo
```

## Properties

- `OrganizationAddress` (string): The organization’s address. Use the LF character (`&#10`) to insert line breaks. This value is available in iOS 7 and later, macOS 10.11 and later, and tvOS 9 and later.
- `OrganizationEmail` (string): The organization’s support email address. This value is available in iOS 7 and later, macOS 10.11 and later, and tvOS 9 and later.
- `OrganizationMagic` (string): A unique identifier for the various services a single organization manages. This value is available in iOS 7 and later, macOS 10.11 and later, and tvOS 9 and later.
- `OrganizationName` (string) *(required)*: A string that describes the organization operating the MDM server. This value is available in iOS 7 and later, macOS 10.11 and later, and tvOS 9 and later.
- `OrganizationPhone` (string): The organization’s phone number. This value is available in iOS 7 and later, macOS 10.11 and later, and tvOS 9 and later.

## See Also

- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](deviceinformationresponse/queryresponses-data.dictionary/accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](deviceinformationresponse/queryresponses-data.dictionary/mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OSUpdateSettings](deviceinformationresponse/queryresponses-data.dictionary/osupdatesettings-data.dictionary.md)
  The response dictionary that contains operating system update settings.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.
- [object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings](deviceinformationresponse/queryresponses-data.dictionary/softwareupdatesettings-data.dictionary.md)
  The response dictionary that contains information about the Software Update pane in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/organizationinfo-data.dictionary)*