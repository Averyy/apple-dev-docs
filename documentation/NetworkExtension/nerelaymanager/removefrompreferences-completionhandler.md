# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Remove your relay configuration from the system networking preferences.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromPreferences() async throws
```

#### Discussion

After you remove your configuration, the [`NERelayManager`](nerelaymanager.md) object still contains the configuration parameters. Calling [`loadFromPreferences(completionHandler:)`](nerelaymanager/loadfrompreferences(completionhandler:).md) clears out the configuration parameters from the [`NERelayManager`](nerelaymanager.md) object.

## Parameters

- `completionHandler`: An optional block that takes an   object. If specified, this block runs on your application’s main thread after your configuration is removed. If an error occurs while removing the configuration, the block returns an   object.

## See Also

- [class func shared() -> NERelayManager](nerelaymanager/shared.md)
  Access the single instance of a network relay manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/loadfrompreferences(completionhandler:).md)
  Load your relay configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/savetopreferences(completionhandler:).md)
  Save your relay configuration to the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/removefrompreferences(completionhandler:))*