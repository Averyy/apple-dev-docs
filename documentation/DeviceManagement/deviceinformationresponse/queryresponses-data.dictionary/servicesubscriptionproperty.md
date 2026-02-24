# DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that contains information about the active service subscription.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty
```

## Properties

- `CarrierSettingsVersion` (string): The version of the carrier settings. This value is available in iOS 12 and later.
- `CurrentCarrierNetwork` (string): The name of the current carrier network. This value is available in iOS 12 and later.
- `CurrentMCC` (string): The current mobile country code (MCC). This value is available in iOS 12 and later.
- `CurrentMNC` (string): The current mobile network code (MNC). This value is available in iOS 12 and later.
- `EID` (string): The eSIM identifier. This value is available in iOS 14 and later.
- `ICCID` (string): The integrated circuit card identifier (ICCID) value. This value is available in iOS 12 and later.
- `IMEI` (string): The device International Mobile Equipment Identity (IMEI) number. This value is available in iOS 12 and later.
- `IsDataPreferred` (boolean): If `true`, this subscription is the preference for data. This value is available in iOS 12 and later.
- `IsRoaming` (boolean): If `true`, the phone is roaming. This value is available in iOS 12 and later.
- `IsVoicePreferred` (boolean): If `true`, this subscription is the preference for voice. This value is available in iOS 12 and later.
- `Label` (string): The label of this subscription. This value is available in iOS 12 and later.
- `LabelID` (string): The unique identifier for this subscription. This value is available in iOS 12 and later.
- `MEID` (string): The device Mobile Equipment Identifier (MEID) number. This query is available in iOS 12 and later.
- `PhoneNumber` (string): The raw phone number without punctuation and including country code. This value is available in iOS 12 and later.
- `Slot` (string): The description of the slot that contains the SIM representing this subscription. This value is available in iOS 12 and later.
- `SubscriberCarrierNetwork` (string): The name of the home carrier network. This value is available in iOS 16 and later.

## See Also

- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](deviceinformationresponse/queryresponses-data.dictionary/accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](deviceinformationresponse/queryresponses-data.dictionary/mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OSUpdateSettings](deviceinformationresponse/queryresponses-data.dictionary/osupdatesettings-data.dictionary.md)
  The response dictionary that contains operating system update settings.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](deviceinformationresponse/queryresponses-data.dictionary/organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.
- [object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings](deviceinformationresponse/queryresponses-data.dictionary/softwareupdatesettings-data.dictionary.md)
  The response dictionary that contains information about the Software Update pane in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty)*