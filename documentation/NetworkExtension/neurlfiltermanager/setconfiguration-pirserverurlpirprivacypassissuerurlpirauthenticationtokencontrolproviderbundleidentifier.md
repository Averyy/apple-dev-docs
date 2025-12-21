# setConfiguration(pirServerURL:pirPrivacyPassIssuerURL:pirAuthenticationToken:controlProviderBundleIdentifier:)

**Framework**: Network Extension  
**Kind**: method

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

- `pirServerURL`: The PIR server URL.  The URL must contain only the domain name of the PIR server.
- `pirPrivacyPassIssuerURL`: The PIR Privacy Pass issuer URL. The URL must contain only the domain name of the Privacy Pass issuer. If nil, the configuration uses the PIR server URL as the Privacy Pass issuer URL.
- `pirAuthenticationToken`: An HTTP bearer token that authenticates the person using your app. The system uses this token to attest that it’s a valid user when requesting anonymous authentication tokens.
- `controlProviderBundleIdentifier`: The bundle identifier of the   app extension.

## See Also

- [func loadFromPreferences() async throws](neurlfiltermanager/loadfrompreferences.md)
  Loads the current URL filter configuration from the caller’s URL filter preferences.
- [func saveToPreferences() async throws](neurlfiltermanager/savetopreferences.md)
  Saves the URL filter configuration in the caller’s URL filter preferences.
- [func removeFromPreferences() async throws](neurlfiltermanager/removefrompreferences.md)
  Removes the URL filter configuration from the caller’s URL filter preferences.
- [func handleConfigChange() -> any AsyncSequence<Bool, Never>](neurlfiltermanager/handleconfigchange.md)
  Sets up an observer for the filter configuration change notification and models it as an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/setconfiguration(pirserverurl:pirprivacypassissuerurl:pirauthenticationtoken:controlproviderbundleidentifier:))*