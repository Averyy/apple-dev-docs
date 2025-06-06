# saveToPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Save the filter configuration in the Network Extension preferences.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func saveToPreferences() async throws
```

#### Discussion

You must call `loadFromPreferencesWithCompletionHandler:` at least once before calling this method the first time after your app launches.

## Parameters

- `completionHandler`: A block that takes an   object. This block will be executed on the caller’s main thread after the save operation is complete. If the configuration could not be saved to the preferences, the error parameter will be set to an   object containing details about the error. See   for a list of possible errors. If the configuration is saved successfully then the error parameter will be set to nil.

## See Also

- [class func shared() -> NEFilterManager](nefiltermanager/shared.md)
  Access the single instance of `NEFilterManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nefiltermanager/loadfrompreferences(completionhandler:).md)
  Load the filter configuration from the Network Extension preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nefiltermanager/removefrompreferences(completionhandler:).md)
  Remove the filter configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltermanager/savetopreferences(completionhandler:))*