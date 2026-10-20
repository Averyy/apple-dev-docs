# DeviceInformationResponse.QueryResponses.MDMOptions

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

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

```
object DeviceInformationResponse.QueryResponses.MDMOptions
```

## Properties

- `ActivationLockAllowedWhileSupervised` (boolean): If `true`, a supervised device registers itself with Activation Lock when the user enables Find My. Unsupervised devices ignore this value.

  Available: iOS 7+ | iPadOS 7+ | macOS 11+ | tvOS 9+

  **Default**: `false`
- `BootstrapTokenAllowed` (boolean): If `true`, the server supports Bootstrap Token commands.

  Available: macOS 11+

  **Default**: `false`
- `PromptUserToAllowBootstrapTokenForAuthentication` (boolean): If `true`, the device can accept a Bootstrap Token from the MDM server instead of prompting for user authentication prior to installation. This only applies when `BootstrapTokenAllowedForAuthentication` is `true` in the [`SecurityInfoResponse.SecurityInfo`](../../securityinforesponse/securityinfo-data.dictionary.md) response. This value is available for a Mac with Apple silicon in macOS 11 and later.

  Available: macOS 11+

  **Default**: `false`

## See Also

### Objects
- [object DeviceInformationResponse.QueryResponses.AccessibilitySettings](./accessibilitysettings-data.dictionary.md)
  The response dictionary that contains the devices accessibility settings.
- [object DeviceInformationResponse.QueryResponses.AutoSetupAdminAccountsItem](./autosetupadminaccountsitem.md)
  The response dictionary that contains the administrator setup information.
- [object DeviceInformationResponse.QueryResponses.OSUpdateSettings](./osupdatesettings-data.dictionary.md)
  The response dictionary that contains operating system update settings.
- [object DeviceInformationResponse.QueryResponses.OrganizationInfo](./organizationinfo-data.dictionary.md)
  The response dictionary that contains organization information.
- [object DeviceInformationResponse.QueryResponses.ServiceSubscriptionProperty](./servicesubscriptionproperty.md)
  The response dictionary that contains information about the active service subscription.
- [object DeviceInformationResponse.QueryResponses.SoftwareUpdateSettings](./softwareupdatesettings-data.dictionary.md)
  The response dictionary that contains information about the Software Update pane in Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/deviceinformationresponse/queryresponses-data.dictionary/mdmoptions-data.dictionary)*