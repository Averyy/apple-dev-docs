# loadFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Loads the current DNS proxy configuration from the caller’s DNS proxy preferences.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func loadFromPreferences() async throws
```

#### Discussion

Initially, the DNS proxy configuration comes from a configuration profile stored on the device in a managed environment, as described in [`Configuration Profile Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206).

When you want to inspect or make changes to the configuration, you call the proxy manager’s [`loadFromPreferences(completionHandler:)`](nednsproxymanager/loadfrompreferences(completionhandler:).md) method. This causes the system to load the configuration into the manager’s [`providerProtocol`](nednsproxymanager/providerprotocol.md) and [`isEnabled`](nednsproxymanager/isenabled.md) properties.

If you modify the configuration stored in these properties, you must then call the [`saveToPreferences(completionHandler:)`](nednsproxymanager/savetopreferences(completionhandler:).md) method to make the changes take effect. Saving the preferences also stores the modified configuration on disk for use the next time the proxy is started or the configuration is loaded.

## Parameters

- `completionHandler`: A block called when the load operation completes. If the operation fails, an error instance passed to this block describes the problem. Otherwise, the error is  . See   for the list of possible errors.

## See Also

- [class func shared() -> NEDNSProxyManager](nednsproxymanager/shared.md)
  Returns a singleton DNS proxy manager instance.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/savetopreferences(completionhandler:).md)
  Saves the DNS proxy configuration in the caller’s DNS proxy preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/removefrompreferences(completionhandler:).md)
  Removes the DNS proxy configuration from the caller’s DNS proxy preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/loadfrompreferences(completionhandler:))*