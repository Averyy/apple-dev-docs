# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Removes the manager’s configuration from the persistent store.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromPreferences() async throws
```

## Parameters

- `completionHandler`: A completion block that the framework calls after it removes the configuration. If removal failed, the   parameter indicates the reason for the failure; otherwise, this parameter is  .

## See Also

- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](neapppushmanager/loadfrompreferences(completionhandler:).md)
  Loads the manager’s saved configuration from the persistent store.
- [class func loadAllFromPreferences(completionHandler: ([NEAppPushManager]?, (any Error)?) -> Void)](neapppushmanager/loadallfrompreferences(completionhandler:).md)
  Loads all saved manager configurations asynchronously.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](neapppushmanager/savetopreferences(completionhandler:).md)
  Saves the manager’s configuration in the persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/removefrompreferences(completionhandler:))*