# handleConfigChange()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Sets up an observer for the filter configuration change notification and models it as an asynchronous sequence.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func handleConfigChange() -> any AsyncSequence<Bool, Never>
```

#### Discussion

The [`AsyncSequence`](../../Swift/asyncsequence.md) created by this method produces a Boolean `true` value every time the filter posts the [`NEURLFilterConfigurationDidChange`](../../Foundation/nsnotification/name-swift.struct/neurlfilterconfigurationdidchange.md) notification.

Use this method to watch for the configuration change notification and react to it.

## See Also

### Working with the filter configuration
- [func setConfiguration(pirServerURL: URL, pirPrivacyPassIssuerURL: URL?, pirAuthenticationToken: String, controlProviderBundleIdentifier: String) throws](./setconfiguration%28pirserverurl,pirprivacypassissuerurl,pirauthenticationtoken,controlproviderbundleidentifier%29.md)
  Sets a URL filter configuration with the required PIR server attributes and app extension information.
- [func loadFromPreferences() async throws](./loadfrompreferences%28%29.md)
  Loads the current URL filter configuration from the caller’s URL filter preferences.
- [func saveToPreferences() async throws](./savetopreferences%28%29.md)
  Saves the URL filter configuration in the caller’s URL filter preferences.
- [func removeFromPreferences() async throws](./removefrompreferences%28%29.md)
  Removes the URL filter configuration from the caller’s URL filter preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/handleconfigchange())*