# loadFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Loads the current DNS proxy configuration from the caller’s DNS proxy preferences.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func loadFromPreferences(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func loadFromPreferences() async throws
```

```objc
- (void) loadFromPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

Initially, the DNS proxy configuration comes from a configuration profile stored on the device in a managed environment, as described in [Configuration Profile Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206).

When you want to inspect or make changes to the configuration, you call the proxy manager’s [`loadFromPreferences(completionHandler:)`](./loadfrompreferences%28completionhandler%29.md) method. This causes the system to load the configuration into the manager’s [`providerProtocol`](./providerprotocol.md) and [`isEnabled`](./isenabled.md) properties.

If you modify the configuration stored in these properties, you must then call the [`saveToPreferences(completionHandler:)`](./savetopreferences%28completionhandler%29.md) method to make the changes take effect. Saving the preferences also stores the modified configuration on disk for use the next time the proxy is started or the configuration is loaded.

## Parameters

- `completionHandler`: A block called when the load operation completes. If the operation fails, an error instance passed to this block describes the problem. Otherwise, the error is `nil`. See [`NEDNSProxyManagerError`](../nednsproxymanagererror.md) for the list of possible errors.

## See Also

### Managing the DNS proxy configuration
- [class func shared() -> NEDNSProxyManager](./shared%28%29.md)
  Returns a singleton DNS proxy manager instance.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Saves the DNS proxy configuration in the caller’s DNS proxy preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./removefrompreferences%28completionhandler%29.md)
  Removes the DNS proxy configuration from the caller’s DNS proxy preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/loadfrompreferences(completionhandler:))*