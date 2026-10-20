# saveToPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Saves the DNS proxy configuration in the caller’s DNS proxy preferences.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func saveToPreferences(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func saveToPreferences() async throws
```

```objc
- (void) saveToPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

If you alter the DNS proxy configuration that you load into the proxy manager’s properties using a call to the [`loadFromPreferences(completionHandler:)`](./loadfrompreferences%28completionhandler%29.md) method, you must then call the [`saveToPreferences(completionHandler:)`](./savetopreferences%28completionhandler%29.md) method to make the changes take effect. Saving also stores the modified configuration for the next time the proxy is started or the configuration loaded.

Trying to save preferences before loading them produces an error.

If the DNS proxy is enabled, it becomes active as a result of this call.

## Parameters

- `completionHandler`: A block called when the save operation completes. If the operation fails, an error instance passed to this block describes the problem. Otherwise, the error is `nil`. See [`NEDNSProxyManagerError`](../nednsproxymanagererror.md) for the list of possible errors.

## See Also

### Managing the DNS proxy configuration
- [class func shared() -> NEDNSProxyManager](./shared%28%29.md)
  Returns a singleton DNS proxy manager instance.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Loads the current DNS proxy configuration from the caller’s DNS proxy preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./removefrompreferences%28completionhandler%29.md)
  Removes the DNS proxy configuration from the caller’s DNS proxy preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednsproxymanager/savetopreferences(completionhandler:))*