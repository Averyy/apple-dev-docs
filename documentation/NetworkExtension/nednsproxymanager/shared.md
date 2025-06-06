# shared()

**Framework**: Network Extension  
**Kind**: method

Returns a singleton DNS proxy manager instance.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class func shared() -> NEDNSProxyManager
```

#### Return Value

The [`NEDNSProxyManager`](nednsproxymanager.md) instance for the app.

#### Discussion

Each app is allowed to create a single DNS proxy manager. The [`shared()`](nednsproxymanager/shared().md) type method returns a singleton [`NEDNSProxyManager`](nednsproxymanager.md) instance that your app can use to manage any DNS proxy instances that it creates.

## See Also

- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/loadfrompreferences(completionhandler:).md)
  Loads the current DNS proxy configuration from the caller’s DNS proxy preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/savetopreferences(completionhandler:).md)
  Saves the DNS proxy configuration in the caller’s DNS proxy preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/removefrompreferences(completionhandler:).md)
  Removes the DNS proxy configuration from the caller’s DNS proxy preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/shared())*