# saveToPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Save your relay configuration to the system networking preferences.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func saveToPreferences() async throws
```

#### Discussion

You must call [`loadFromPreferences(completionHandler:)`](nerelaymanager/loadfrompreferences(completionhandler:).md) at least once before calling this method the first time after your app launches.

## Parameters

- `completionHandler`: An optional block that takes an   object. If specified, this block runs on your application’s main thread after the save operation completes. If an error occurs while saving the configuration, the block returns an   object.

## See Also

- [class func shared() -> NERelayManager](nerelaymanager/shared.md)
  Access the single instance of a network relay manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/loadfrompreferences(completionhandler:).md)
  Load your relay configuration from the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/removefrompreferences(completionhandler:).md)
  Remove your relay configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/savetopreferences(completionhandler:))*