# SettingsResponse.Settings

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

A dictionary that describes the results of configuring settings on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```
object SettingsResponse.Settings
```

## Topics

### Objects
- [object SettingsResponse.Settings.ErrorChainItem](./settings-data.dictionary/errorchainitem.md)
  A dictionary that describes an error chain item.

## Properties

- `ErrorChain` ([SettingsResponse.Settings.ErrorChainItem]): An array of dictionaries that describes any errors that occurred.
- `Identifier` (string): The app identifier to which this error applies.

  > **Note**:  For a watchOS app, the identifier is the watch’s bundle identifier, which differs from the main bundle identifier for the iPhone the watch pairs with.

  Available: iOS 7+ | iPadOS 7+ | tvOS 10.2+ | visionOS 1.1+ | watchOS 10+
- `Status` (string) *(required)*: The status of the setting, which is one of the following values:

  - `Acknowledged`: The device processed the command successfully.
  - `Error`: An error occurred. See the `ErrorChain` for more details.

## See Also

### Objects
- [object SettingsResponse.ErrorChainItem](./errorchainitem.md)
  A dictionary that describes an error chain item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/settingsresponse/settings-data.dictionary)*