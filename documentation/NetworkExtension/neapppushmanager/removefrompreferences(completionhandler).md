# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Removes the manager’s configuration from the persistent store.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromPreferences(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func removeFromPreferences() async throws
```

```objc
- (void) removeFromPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A completion block that the framework calls after it removes the configuration. If removal failed, the `error` parameter indicates the reason for the failure; otherwise, this parameter is `nil`.

## See Also

### Persisting manager settings
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Loads the manager’s saved configuration from the persistent store.
- [class func loadAllFromPreferences(completionHandler: ([NEAppPushManager]?, (any Error)?) -> Void)](./loadallfrompreferences%28completionhandler%29.md)
  Loads all saved manager configurations asynchronously.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Saves the manager’s configuration in the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/removefrompreferences(completionhandler:))*