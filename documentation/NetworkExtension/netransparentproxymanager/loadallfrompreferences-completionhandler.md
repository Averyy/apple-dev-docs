# loadAllFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Loads all previously-saved transparent proxy configurations.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func loadAllFromPreferences() async throws -> [NETransparentProxyManager]
```

#### Discussion

This method asychronously reads all previously-saved transparent proxy configurations associated with the calling app.

## Parameters

- `completionHandler`: A Swift closure or an ObjectiveC block that receives as parameters   an array of transparent proxy manager instances loaded from disk and an error.   If the error is  , no error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netransparentproxymanager/loadallfrompreferences(completionhandler:))*