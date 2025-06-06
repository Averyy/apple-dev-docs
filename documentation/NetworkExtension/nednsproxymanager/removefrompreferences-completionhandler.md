# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Removes the DNS proxy configuration from the caller’s DNS proxy preferences.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func removeFromPreferences() async throws
```

#### Discussion

If you use a device without an installed configuration profile during development, your app can create the DNS proxy configuration from scratch. You first call the [`loadFromPreferences(completionHandler:)`](nednsproxymanager/loadfrompreferences(completionhandler:).md) method to retrieve the empty configuration. You then make updates and call the [`saveToPreferences(completionHandler:)`](nednsproxymanager/savetopreferences(completionhandler:).md) method to store them. To remove the configuration, call the [`removeFromPreferences(completionHandler:)`](nednsproxymanager/removefrompreferences(completionhandler:).md) method. This allows you to restore the device to a clean, unconfigured state.

In a production environment, however, a configuration profile placed in the system by an external process typically provides the baseline DNS proxy configuration. Your app can modify this configuration at runtime using the same load-modify-save steps, but cannot remove the configuration entirely. An attempt to remove the configuration when a configuration profile is present on the device results in a [`NEDNSProxyManagerError.configurationCannotBeRemoved`](nednsproxymanagererror/configurationcannotberemoved.md) error.

If the DNS proxy is enabled, it becomes disabled as a result of this call.

## Parameters

- `completionHandler`: A block called when the remove operation completes. If the operation fails, an error instance passed to this block describes the problem. Otherwise, the error is  . See   for the list of possible errors.

## See Also

- [class func shared() -> NEDNSProxyManager](nednsproxymanager/shared.md)
  Returns a singleton DNS proxy manager instance.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/loadfrompreferences(completionhandler:).md)
  Loads the current DNS proxy configuration from the caller’s DNS proxy preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/savetopreferences(completionhandler:).md)
  Saves the DNS proxy configuration in the caller’s DNS proxy preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/removefrompreferences(completionhandler:))*