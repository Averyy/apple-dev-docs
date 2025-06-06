# loadFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Load your relay configuration from the system networking preferences.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func loadFromPreferences() async throws
```

#### Discussion

You must call this method at least once before calling [`saveToPreferences(completionHandler:)`](nerelaymanager/savetopreferences(completionhandler:).md) for the first time after your app launches.

## Parameters

- `completionHandler`: A block that takes an   object. This block runs on your application’s main thread after the load operation is complete. If an error occurs while loading the configuration, the block returns an   object.

## See Also

- [class func shared() -> NERelayManager](nerelaymanager/shared.md)
  Access the single instance of a network relay manager.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/savetopreferences(completionhandler:).md)
  Save your relay configuration to the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/removefrompreferences(completionhandler:).md)
  Remove your relay configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/loadfrompreferences(completionhandler:))*