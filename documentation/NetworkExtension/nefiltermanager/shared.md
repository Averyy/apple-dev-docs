# shared()

**Framework**: Network Extension  
**Kind**: method

Access the single instance of `NEFilterManager`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class func shared() -> NEFilterManager
```

#### Return Value

The `NEFilterManager` instance for the calling application.

## See Also

- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nefiltermanager/loadfrompreferences(completionhandler:).md)
  Load the filter configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nefiltermanager/savetopreferences(completionhandler:).md)
  Save the filter configuration in the Network Extension preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nefiltermanager/removefrompreferences(completionhandler:).md)
  Remove the filter configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/shared())*