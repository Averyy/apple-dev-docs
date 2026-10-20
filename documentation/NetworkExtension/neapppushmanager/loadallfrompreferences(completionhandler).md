# loadAllFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Loads all saved manager configurations asynchronously.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class func loadAllFromPreferences(completionHandler: @escaping @Sendable ([NEAppPushManager]?, (any Error)?) -> Void)
```

```swift
class func loadAllFromPreferences() async throws -> [NEAppPushManager]
```

```objc
+ (void) loadAllFromPreferencesWithCompletionHandler:(void (^)(NSArray<NEAppPushManager *> *managers, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A completion block that the framework calls after it loads the configurations. The `managers` parameter contains an array of all managers that the framework loads from the persistent store. This array is empty if the framework didn’t load any configurations. If loading failed, the `error` parameter indicates the reason for the failure; otherwise, this parameter is `nil`.

## See Also

### Persisting manager settings
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Loads the manager’s saved configuration from the persistent store.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Saves the manager’s configuration in the persistent store.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./removefrompreferences%28completionhandler%29.md)
  Removes the manager’s configuration from the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/loadallfrompreferences(completionhandler:))*