# shared()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NEDNSProxyManager *) sharedManager;
```

#### Return Value

The [`NEDNSProxyManager`](../nednsproxymanager.md) instance for the app.

#### Discussion

Each app is allowed to create a single DNS proxy manager. The [`shared()`](./shared%28%29.md) type method returns a singleton [`NEDNSProxyManager`](../nednsproxymanager.md) instance that your app can use to manage any DNS proxy instances that it creates.

## See Also

### Managing the DNS proxy configuration
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Loads the current DNS proxy configuration from the caller’s DNS proxy preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Saves the DNS proxy configuration in the caller’s DNS proxy preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./removefrompreferences%28completionhandler%29.md)
  Removes the DNS proxy configuration from the caller’s DNS proxy preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/shared())*