# shared()

**Framework**: Network Extension  
**Kind**: method

Access the single instance of a network relay manager.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func shared() -> NERelayManager
```

#### Return Value

The network relay manager instance for the calling application.

## See Also

- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/loadfrompreferences(completionhandler:).md)
  Load your relay configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/savetopreferences(completionhandler:).md)
  Save your relay configuration to the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nerelaymanager/removefrompreferences(completionhandler:).md)
  Remove your relay configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager/shared())*