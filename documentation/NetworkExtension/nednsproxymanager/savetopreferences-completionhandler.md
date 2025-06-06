# saveToPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Saves the DNS proxy configuration in the caller’s DNS proxy preferences.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func saveToPreferences() async throws
```

#### Discussion

If you alter the DNS proxy configuration that you load into the proxy manager’s properties using a call to the [`loadFromPreferences(completionHandler:)`](nednsproxymanager/loadfrompreferences(completionhandler:).md) method, you must then call the [`saveToPreferences(completionHandler:)`](nednsproxymanager/savetopreferences(completionhandler:).md) method to make the changes take effect. Saving also stores the modified configuration for the next time the proxy is started or the configuration loaded.

Trying to save preferences before loading them produces an error.

If the DNS proxy is enabled, it becomes active as a result of this call.

## Parameters

- `completionHandler`: A block called when the save operation completes. If the operation fails, an error instance passed to this block describes the problem. Otherwise, the error is  . See   for the list of possible errors.

## See Also

- [class func shared() -> NEDNSProxyManager](nednsproxymanager/shared.md)
  Returns a singleton DNS proxy manager instance.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/loadfrompreferences(completionhandler:).md)
  Loads the current DNS proxy configuration from the caller’s DNS proxy preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nednsproxymanager/removefrompreferences(completionhandler:).md)
  Removes the DNS proxy configuration from the caller’s DNS proxy preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/savetopreferences(completionhandler:))*