# removeFromPreferences()

**Framework**: Network Extension  
**Kind**: method

Removes the URL filter configuration from the caller’s URL filter preferences.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func removeFromPreferences() async throws
```

#### Discussion

If the URL filter is enabled, this call disables it.

## See Also

- [func setConfiguration(pirServerURL: URL, pirPrivacyPassIssuerURL: URL?, pirAuthenticationToken: String, controlProviderBundleIdentifier: String) throws](neurlfiltermanager/setconfiguration(pirserverurl:pirprivacypassissuerurl:pirauthenticationtoken:controlproviderbundleidentifier:).md)
  Sets a URL filter configuration with the required PIR server attributes and app extension information.
- [func loadFromPreferences() async throws](neurlfiltermanager/loadfrompreferences.md)
  Loads the current URL filter configuration from the caller’s URL filter preferences.
- [func saveToPreferences() async throws](neurlfiltermanager/savetopreferences.md)
  Saves the URL filter configuration in the caller’s URL filter preferences.
- [func handleConfigChange() -> any AsyncSequence<Bool, Never>](neurlfiltermanager/handleconfigchange.md)
  Sets up an observer for the filter configuration change notification and models it as an asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/removefrompreferences())*