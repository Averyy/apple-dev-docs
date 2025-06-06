# loadFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Loads the manager’s saved configuration from the persistent store.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func loadFromPreferences() async throws
```

## Parameters

- `completionHandler`: A completion block that the framework calls after it loads the configuration. If loading failed, the   parameter indicates the reason for the failure; otherwise, this parameter is  .

## See Also

- [class func loadAllFromPreferences(completionHandler: ([NEAppPushManager]?, (any Error)?) -> Void)](neapppushmanager/loadallfrompreferences(completionhandler:).md)
  Loads all saved manager configurations asynchronously.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](neapppushmanager/savetopreferences(completionhandler:).md)
  Saves the manager’s configuration in the persistent store.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](neapppushmanager/removefrompreferences(completionhandler:).md)
  Removes the manager’s configuration from the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/loadfrompreferences(completionhandler:))*