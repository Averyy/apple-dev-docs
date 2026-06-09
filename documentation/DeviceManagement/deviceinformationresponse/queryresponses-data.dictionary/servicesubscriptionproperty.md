# DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that contains information about the active service subscription.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+

## Declaration

```swift
object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty
```

## Properties

- `CarrierSettingsVersion` (string): The version of the carrier settings.
- `CurrentCarrierNetwork` (string): The name of the current carrier network.
- `CurrentMCC` (string): The current mobile country code (MCC).
- `CurrentMNC` (string): The current mobile network code (MNC).
- `EID` (string): The eSIM identifier. Available: iOS 14+ | iPadOS 14+
- `ICCID` (string): The integrated circuit card identifier (ICCID) value.
- `IMEI` (string): The device International Mobile Equipment Identity (IMEI) number.
- `IsDataPreferred` (boolean): If `true`, this subscription is the preference for data.
- `IsRoaming` (boolean): If `true`, the phone is roaming.
- `IsVoicePreferred` (boolean): If `true`, this subscription is the preference for voice.
- `Label` (string): The label of this subscription.
- `LabelID` (string): The unique identifier for this subscription.
- `MEID` (string): The device Mobile Equipment Identifier (MEID) number.
- `PhoneNumber` (string): The raw phone number without punctuation and including country code.
- `Slot` (string): The description of the slot that contains the SIM representing this subscription.
- `SubscriberCarrierNetwork` (string): The name of the home carrier network. Available: iOS 16+ | iPadOS 16+

## See Also

- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](deviceinformationresponse/queryresponses-data.dictionary/accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.MDMOptions](deviceinformationresponse/queryresponses-data.dictionary/mdmoptions-data.dictionary.md)
  The response dictionary that contains MDM options.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](deviceinformationresponse/queryresponses-data.dictionary/organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty)*