# setConfiguration(pirServerURL:pirPrivacyPassIssuerURL:pirAuthenticationToken:controlProviderBundleIdentifier:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Sets a URL filter configuration with the required PIR server attributes and app extension information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func setConfiguration(pirServerURL: URL, pirPrivacyPassIssuerURL: URL?, pirAuthenticationToken: String, controlProviderBundleIdentifier: String) throws
```

## Parameters

- `pirServerURL`: The PIR server URL.  The URL must contain only the domain name of the PIR server, and must match the value defined in the `NSPIRConfiguration` dictionary in the information property list.
- `pirPrivacyPassIssuerURL`: The PIR Privacy Pass issuer URL. The URL must contain only the domain name of the Privacy Pass issuer. If `nil`, the configuration uses the PIR server URL as the Privacy Pass issuer URL. This value must match the value defined in the `NSPIRConfiguration` dictionary in the information property list.
- `pirAuthenticationToken`: An HTTP bearer token that authenticates the person using your app. The system uses this token to attest that it’s a valid user when requesting anonymous authentication tokens.
- `controlProviderBundleIdentifier`: The bundle identifier of the [`NEURLFilterControlProvider`](../neurlfiltercontrolprovider.md) app extension.

## See Also

### Working with the filter configuration
- [func loadFromPreferences() async throws](./loadfrompreferences%28%29.md)
  Loads the current URL filter configuration from the caller’s URL filter preferences.
- [func saveToPreferences() async throws](./savetopreferences%28%29.md)
  Saves the URL filter configuration in the caller’s URL filter preferences.
- [func removeFromPreferences() async throws](./removefrompreferences%28%29.md)
  Removes the URL filter configuration from the caller’s URL filter preferences.
- [func handleConfigChange() -> any AsyncSequence<Bool, Never>](./handleconfigchange%28%29.md)
  Sets up an observer for the filter configuration change notification and models it as an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/setconfiguration(pirserverurl:pirprivacypassissuerurl:pirauthenticationtoken:controlproviderbundleidentifier:))*