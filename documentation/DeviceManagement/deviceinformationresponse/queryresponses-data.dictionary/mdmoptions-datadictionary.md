# DeviceInformationResponse.QueryResponses.MDMOptions

**Framework**: Device Management  
**Kind**: dictionary

The response dictionary that contains MDM options.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 11.0+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object DeviceInformationResponse.QueryResponses.MDMOptions
```

## Properties

- `ActivationLockAllowedWhileSupervised` (boolean): If `true`, a supervised device registers itself with Activation Lock when the user enables Find My. Unsupervised devices ignore this value. Available: iOS 7+ | iPadOS 7+ | macOS 11+ | tvOS 9+
- `BootstrapTokenAllowed` (boolean): If `true`, the server supports Bootstrap Token commands. Available: macOS 11+
- `PromptUserToAllowBootstrapTokenForAuthentication` (boolean): If `true`, the device can accept a Bootstrap Token from the MDM server instead of prompting for user authentication prior to installation. This only applies when `BootstrapTokenAllowedForAuthentication` is `true` in the [`SecurityInfoResponse.SecurityInfo`](securityinforesponse/securityinfo-data.dictionary.md) response. This value is available for a Mac with Apple silicon in macOS 11 and later. Available: macOS 11+

## See Also

- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](deviceinformationresponse/queryresponses-data.dictionary/accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](deviceinformationresponse/queryresponses-data.dictionary/autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](deviceinformationresponse/queryresponses-data.dictionary/organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](deviceinformationresponse/queryresponses-data.dictionary/servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/mdmoptions-data.dictionary)*